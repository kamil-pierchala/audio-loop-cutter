from pathlib import Path
import yt_dlp


def parse_timestamp_to_seconds(timestamp: str) -> float:
    """Convert timestamp strings like 'SS', 'MM:SS' or 'HH:MM:SS' into total seconds."""
    # split the string by colon into individual numeric chunks
    parts = list(map(float, timestamp.strip().split(":")))

    if len(parts) == 1:
        # user passed only seconds, for example "45"
        return parts[0]
    elif len(parts) == 2:
        # user passed minutes and seconds, for example "01:30" -> 1*60 + 30
        return parts[0] * 60 + parts[1]
    elif len(parts) == 3:
        # user passed hours, minutes and seconds, for example  "01:05:20" -> 1*3600 + 5*60 + 20
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    else:
        raise ValueError(
            f"Invalid timestamp format: '{timestamp}'. Expected 'SS', 'MM:SS', or 'HH:MM:SS'."
        )


def download_audio_clip(
    url: str,
    start_time: str,
    end_time: str,
    output_dir: Path = Path("output"),
    audio_format: str = "mp3",
) -> Path:
    """Download and trim a specific audio section from a given URL."""
    # make sure the target directory exists on the disk (creates it if it's missing)
    output_dir.mkdir(parents=True, exist_ok=True)

    start_sec = parse_timestamp_to_seconds(start_time)
    end_sec = parse_timestamp_to_seconds(end_time)

    # basic boundary check
    if start_sec >= end_sec:
        raise ValueError("Start time must be smaller than end time.")

    # file naming pattern for yt-dlp <Title>_<start>-<end>.<extension>
    out_template = str(
        output_dir / "%(title)s_%(section_start)s-%(section_end)s.%(ext)s"
    )

    # yt-dlp configuration dictionary
    ydl_opts = {
        # select best available audio stream
        "format": "bestaudio/best",
        # set where and how to save the file
        "outtmpl": out_template,
        "quiet": False,
        "no_warnings": True,
        # instruct yt-dlp to download ONLY the specified time range
        "download_ranges": yt_dlp.utils.download_range_func(
            None, [(start_sec, end_sec)]
        ),
        "force_keyframes_at_cuts": True,
        # post-process the file using FFmpeg to turn it into an MP3 or WAV
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": audio_format,
                "preferredquality": "192",
            }
        ],
    }

    # context manager handles setup and teardown automatically
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return output_dir
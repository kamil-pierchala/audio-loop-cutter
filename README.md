# Audio Loop Cutter (CLI)

A lightweight command-line tool built with Python to extract and trim specific audio clips from online video/audio sources (e.g. YouTube) for music practice, vocal training, or sampling.

Powered by `yt-dlp`, `typer`, `rich`, and `ffmpeg`.

---

## Features

- **Selective Downloading**: Downloads only the specified time range instead of the entire stream, saving bandwidth and disk space.
- **Timestamp Flexibility**: Supports `SS`, `MM:SS`, and `HH:MM:SS` input formats.
- **Audio Conversion**: Automatically converts trimmed audio to `.mp3` or `.wav` via FFmpeg.
- **Clean CLI Experience**: Styled terminal interface with clear error reporting and progress details.

---

## Prerequisites

- **Python 3.11+**
- **FFmpeg** installed and accessible in your system `PATH`:
  - On Windows: `winget install Gyan.FFmpeg`
  - On macOS: `brew install ffmpeg`
  - On Linux: `sudo apt install ffmpeg`

---
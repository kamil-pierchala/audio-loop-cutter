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

## Installation

1. **Clone the repository:**
  ```
   git clone [https://github.com/kamil-pierchala/audio-loop-cutter.git](https://github.com/kamil-pierchala/audio-loop-cutter.git)
   cd audio-loop-cutter
  ```
2. **Create and activate a virtual environment:**
  ```
    python -m venv .venv
    # Windows (PowerShell):
    .venv\Scripts\Activate.ps1
    # Linux / macOS:
    source .venv/bin/activate
  ```
3. **Install dependencies:**
  ```
    pip install -r requirements.txt
  ```

---

## Usage
Run the tool using the module syntax:
```
python -m src.audio_cutter.cli cut "<URL>" --start <START_TIME> --end <END_TIME> [OPTIONS]
```

### Options

| Flag | Short | Description | Default |
| :--- | :--- | :--- | :--- |
| `--start` | `-s` | Start time ( `SS` , `MM:SS` , `HH:MM:SS` ) | *Required* |
| `--end` | `-e` | End time ( `SS` , `MM:SS` , `HH:MM:SS` ) | *Required* |
| `--out` | `-o` | Target directory for generated clips | `output` |
| `--format` | `-f` | Output audio format ( `mp3` , `wav` ) | `mp3` |

### Examples

Extract 10 seconds of a guitar riff / drum loop:
```
python -m src.audio_cutter.cli cut "[https://www.youtube.com/watch?v=dQw4w9WgXcQ](https://www.youtube.com/watch?v=dQw4w9WgXcQ)" -s 00:05 -e 00:15
```
Save as uncompressed WAV file:
```
python -m src.audio_cutter.cli cut "[https://www.youtube.com/watch?v=dQw4w9WgXcQ](https://www.youtube.com/watch?v=dQw4w9WgXcQ)" -s 01:20 -e 01:35 -f wav -o samples
```

---

## Running Tests
Execute test suite using pytest:
```
pytest
```

---

## License
This project is licensed under the MIT License.
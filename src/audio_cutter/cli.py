from pathlib import Path
import typer
from rich.console import Console

from .core import download_audio_clip

# create the Typer CLI app instance
app = typer.Typer(
    help="CLI tool to download and trim audio tracks for practice sessions and sampling."
)

# rich console for styled terminal output
console = Console()


@app.command()
def cut(
    url: str = typer.Argument(..., help="Source URL (e.g. YouTube video or track link)"),
    start: str = typer.Option(
        ..., "--start", "-s", help="Start timestamp in SS, MM:SS, or HH:MM:SS format"
    ),
    end: str = typer.Option(
        ..., "--end", "-e", help="End timestamp in SS, MM:SS, or HH:MM:SS format"
    ),
    output: Path = typer.Option(
        Path("output"), "--out", "-o", help="Directory where trimmed audio is saved"
    ),
    audio_format: str = typer.Option(
        "mp3", "--format", "-f", help="Target audio format (e.g. mp3, wav)"
    ),
) -> None:
    """Download and trim a section of an audio track."""
    console.print("[bold cyan]Starting audio extraction...[/bold cyan]")
    console.print(f"URL: [yellow]{url}[/yellow]")
    console.print(f"Range: [green]{start}[/green] -> [green]{end}[/green]")

    try:
        # call our core logic
        download_audio_clip(
            url=url,
            start_time=start,
            end_time=end,
            output_dir=output,
            audio_format=audio_format.lower(),
        )
        console.print(
            f"[bold green]✓ Done![/bold green] Audio saved into: [bold]{output.resolve()}[/bold]"
        )
    except Exception as exc:
        console.print(f"[bold red]Error during processing:[/bold red] {exc}")
        # exit with a non-zero status code to signal failure
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
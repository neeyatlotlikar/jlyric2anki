import typer
from pathlib import Path
from jlyric2anki.analyzer import analyze_line
from jlyric2anki.anki_generator import create_deck
from jlyric2anki.utils import show_loader
from jlyric2anki.audio_generator import generate_audio

app = typer.Typer()
AUDIO_DIR = Path("audio")


@app.command()
def generate_deck(
    lyrics_path: Path = typer.Argument(..., help="Path to lyrics.txt"),
    output_file: str = typer.Option(
        "lyrics_deck.apkg", help="Output Anki deck filename"
    ),
    deck_name: str = typer.Option("Japanese Lyrics Deck", help="Name of the Anki deck"),
    source: str = typer.Option(
        "Lyrics", help="Source of the lyrics (e.g., 'Lyrics', 'Song', 'Album', etc.)"
    ),
):
    if not lyrics_path.exists():
        typer.echo("Lyrics file not found!")
        raise typer.Exit()

    with lyrics_path.open("r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    analyzed = show_loader(
        "Analyzing lyrics...", lambda: [analyze_line(line) for line in lines]
    )

    # Generate audio
    audio_files = show_loader(
        "Generating audio...",
        lambda: [generate_audio(line, AUDIO_DIR, i) for i, line in enumerate(lines)],
    )

    show_loader(
        "Generating Anki deck...",
        create_deck,
        deck_name,
        analyzed,
        output_file,
        source,
        audio_files,
    )
    typer.echo(f"Anki deck created: {output_file}")


if __name__ == "__main__":
    app()

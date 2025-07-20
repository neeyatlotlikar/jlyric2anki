import typer
from pathlib import Path
from jlyric2anki.analyzer import analyze_line
from jlyric2anki.anki_generator import create_deck
from jlyric2anki.utils import show_loader

app = typer.Typer()


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
        lines = [line for line in f.readlines() if line.strip()]

    analyzed = show_loader(
        "Analyzing lyrics...", lambda: [analyze_line(line) for line in lines]
    )
    show_loader(
        "Generating Anki deck...", create_deck, deck_name, analyzed, output_file, source
    )
    typer.echo(f"Anki deck created: {output_file}")


if __name__ == "__main__":
    app()

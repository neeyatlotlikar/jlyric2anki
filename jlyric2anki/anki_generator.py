import os
from textwrap import dedent
from pathlib import Path

import genanki

# Read CSS from file
with open(os.path.join(os.path.dirname(__file__), "style.css"), "r") as css_file:
    css_content = css_file.read()


# Define the Anki model for sentence mining
model = genanki.Model(
    1607392319,
    "Sentence Mining Model",
    fields=[
        {"name": "Kanji"},
        {"name": "Pronunciation"},
        {"name": "Romaji"},
        {"name": "Meaning"},
        {"name": "Source"},
    ],
    templates=[
        {
            "name": "Card",
            "qfmt": "<div class='kanji'>{{Kanji}}</div>",
            "afmt": dedent(
                """{{FrontSide}}<hr id="answer">
                <div class="pronunciation">{{Pronunciation}}</div><br>
                <div class="romaji">{{Romaji}}</div><br>
                <div class="meanings">{{Meaning}}</div><br>
                <div class="source">{{Source}}</div>"""
            ).strip(),
        }
    ],
    css=css_content,
)


def create_deck(
    deck_name: str,
    analyzed_lines: list,
    output_file: str,
    source: str,
    audio_files: list,
):
    deck = genanki.Deck(2059400110, deck_name)
    package = genanki.Package(deck)

    for i, data in enumerate(analyzed_lines):
        audio_tag = f"[sound:{Path(audio_files[i]).name}]" if audio_files else ""
        note = genanki.Note(
            model=model,
            fields=[
                f"{audio_tag}<br><br>{data['kanji']}",
                data["pronunciation"],
                data["romaji"],
                data["meanings"],
                source,
            ],
        )
        deck.add_note(note)

    if audio_files:
        package.media_files = audio_files

    package.write_to_file(output_file)

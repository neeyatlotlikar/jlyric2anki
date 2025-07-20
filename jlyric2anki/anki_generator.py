import os
from textwrap import dedent

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


def create_deck(deck_name: str, analyzed_lines: list, output_file: str, source: str):
    deck = genanki.Deck(2059400110, deck_name)

    for data in analyzed_lines:
        note = genanki.Note(
            model=model,
            fields=[
                data["kanji"],
                data["pronunciation"],
                data["romaji"],
                data["meanings"],
                source,
            ],
        )
        deck.add_note(note)

    genanki.Package(deck).write_to_file(output_file)

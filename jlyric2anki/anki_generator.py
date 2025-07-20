import genanki
import os

# Read CSS from file
with open(os.path.join(os.path.dirname(__file__), "style.css"), "r") as css_file:
    css_content = css_file.read()


# Define the Anki model for sentence mining
model = genanki.Model(
    1607392319,
    "Sentence Mining Model",
    fields=[
        {"name": "Kanji"},
        {"name": "Furigana"},
        {"name": "Romaji"},
        {"name": "Meaning"},
    ],
    templates=[
        {
            "name": "Card",
            "qfmt": "{{Kanji}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{Furigana}}<br><br>{{Romaji}}<br><br>{{Meaning}}',
        }
    ],
    css=css_content,
)


def create_deck(deck_name: str, analyzed_lines: list, output_file: str):
    deck = genanki.Deck(2059400110, deck_name)

    for data in analyzed_lines:
        note = genanki.Note(
            model=model,
            fields=[data["kanji"], data["furigana"], data["romaji"], data["meanings"]],
        )
        deck.add_note(note)

    genanki.Package(deck).write_to_file(output_file)

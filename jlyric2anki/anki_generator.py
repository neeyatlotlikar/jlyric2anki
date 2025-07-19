import genanki

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
            "afmt": '{{FrontSide}}<hr id="answer">{{Furigana}}<br>{{Romaji}}<br>{{Meaning}}',
        }
    ],
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

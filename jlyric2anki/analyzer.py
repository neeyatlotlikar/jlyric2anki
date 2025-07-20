import fugashi
from jamdict import Jamdict


tagger = fugashi.Tagger()
jam = Jamdict()


def analyze_line(line: str):
    tokens = tagger(line)
    furigana_line, romaji_line, meanings = "", "", []

    for token in tokens:
        surface = token.surface
        reading = token.feature.pron or surface
        base = token.feature.lemma or surface

        furigana_line += f"{surface}({reading}) "
        romaji_line += reading + " "

        result = jam.lookup(base)
        if result.entries:
            glossary = [str(entry) for entry in result.entries[0].senses[0].gloss]
            meaning = ", ".join(glossary)
            meanings.append(f"{surface} ({base}): {meaning}")

    kanji_line = f"<ruby>{line.strip()}<rt>{romaji_line.strip()}</rt></ruby> "

    return {
        "kanji": kanji_line.strip(),
        "furigana": furigana_line.strip(),
        "romaji": romaji_line.strip(),
        "meanings": "<br>".join(meanings),
    }

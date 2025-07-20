import fugashi
from jaconv import kata2hira
from jamdict import Jamdict
from utils import is_hiragana, is_japanese, is_kana, is_kanji


tagger = fugashi.Tagger()
jam = Jamdict()


def analyze_line(line: str):
    tokens = tagger(line)
    furigana_line, romaji_line, meanings = "", "", []

    for token in tokens:
        surface = token.surface
        reading = token.feature.pron or surface
        base = token.feature.lemma or surface

        if not is_japanese(surface):
            # Foreign words (in katakana) or punctuation
            reading = reading if str(reading).isalnum() else surface
            furigana_line += f"<ruby>{surface}<rt>{reading}</rt></ruby> "
            romaji_line += reading + " "

        if is_kanji(surface):
            furigana_line += f"<ruby>{surface}<rt>{kata2hira(reading)}</rt></ruby> "
            romaji_line += kata2hira(reading) + " "

        if is_kana(surface):
            furigana_line += f"{surface} "
            romaji_line += (
                kata2hira(reading) if is_hiragana(surface) else reading
            ) + " "

        result = jam.lookup(base)
        if result.entries:
            glossary = [str(entry) for entry in result.entries[0].senses[0].gloss]
            meaning = ", ".join(glossary)
            meanings.append(f"{surface} ({base}): {meaning}")

    kanji_line = (
        f"<ruby>{line.strip()}<rt>{kata2hira(romaji_line.strip())}</rt></ruby> "
    )

    return {
        "kanji": kanji_line.strip(),
        "furigana": furigana_line.strip(),
        "romaji": romaji_line.strip(),
        "meanings": "<br>".join(meanings),
    }

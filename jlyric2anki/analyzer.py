import fugashi
from jaconv import kata2hira, kata2alphabet
from jamdict import Jamdict
from .utils import is_kanji


tagger = fugashi.Tagger()
jam = Jamdict()


def analyze_line(line: str):
    tokens = tagger(line)
    sentence, pronunciation, romaji_line, meanings = "", "", "", []

    for token in tokens:
        surface = token.surface
        reading = token.feature.pron or surface
        reading = reading if str(reading).isalnum() else surface
        base = token.feature.lemma or surface

        if is_kanji(surface):
            # Kanji with furigana
            sentence += f"<ruby>{surface}<rt>{kata2hira(reading)}</rt></ruby> "
        else:
            # Hiragana, Katakana, Non-Japanese characters or Punctuation
            sentence += surface + " "

        pronunciation += reading + " "
        romaji_line += kata2alphabet(reading) + " "

        result = jam.lookup(base)
        if result.entries:
            glossary = [str(entry) for entry in result.entries[0].senses[0].gloss]
            meaning = ", ".join(glossary)
            meanings.append(f"{surface} ({base}): {meaning}")

    return {
        "kanji": sentence.strip(),
        "pronunciation": pronunciation.strip(),
        "romaji": romaji_line.strip(),
        "meanings": "<br>".join(meanings),
    }

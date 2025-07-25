import fugashi
from jaconv import kata2alphabet, kata2hira
from jamdict import Jamdict

from jlyric2anki.translator import translate_sentence
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

    full_translation = translate_sentence(line)

    return {
        "kanji": sentence.strip(),
        "pronunciation": pronunciation.strip(),
        "romaji": romaji_line.strip(),
        "meanings": f"{full_translation}<br><br>" + "<br>".join(meanings),
    }

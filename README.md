# 🎵 jlyric2anki

A CLI tool that converts Japanese song lyrics (in Kanji) into **Anki flashcards** for sentence mining and vocabulary learning.

---

## ✨ Features

- 🧠 Sentence-level mining from Japanese lyrics

- 📖 Auto-generates furigana, romaji, and word meanings

- 🌐 Full-sentence translations using **offline FOSS translator** (Argos Translate)

- 🔊 TTS audio generation (FOSS-supported, `gTTS`)

- 🗂 Outputs an `.apkg` file ready for Anki import

- 🖥 Simple CLI interface

- ⚙️ Uses MeCab (`fugashi`) and `jamdict` for analysis

---

## 📁 Project Structure

```graphql
jlyric2anki/
├── jlyric2anki/
│ ├── analyzer.py # Tokenization, furigana, meaning
│ ├── anki_generator.py # Anki deck creation
│ ├── audio_generator.py # Text-to-Speech
│ |── utils.py # Various utility functions
| |── translator.py # Sentence Translation
| └── style.css # Styling for Anki template
├── tests/
│ ├── test_analyzer.py # Test cases for analyzer.py
│ |── test_utils.py # Test cases for utils.py
│ |── test_audio_generator.py # Test cases for TTS
| └── test_translator.py # Test cases for translator.py
├── cli.py # CLI entry point using Typer
├── requirements.txt # Dependencies
└── README.md
```

---

## 📦 Installation

```bash
git clone https://github.com/neeyatlotlikar/jlyric2anki.git
cd jlyric2anki
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Notes:
# The full version of UniDic (internally used package) requires a separate download step
python -m unidic download

# Run once for argostranslate setup
python -c "from jlyric2anki.translator import setup_argos_translate; setup_argos_translate()"

```

---

## 📝 Usage

Place your Japanese lyrics in lyrics.txt, one sentence per line.

Then run:

```bash
python cli.py generate-deck lyrics.txt --output-file mydeck.apkg --deck-name "My Jpop Deck" --source "From: Song Name by Artist"
```

This will output an Anki deck file like `mydeck.apkg`.

---

## 🧾 Features in Action

- ✅ Full sentence as flashcard

- ✅ Furigana & Romaji auto-generated

- ✅ Word-by-word definitions (via Jamdict)

- ✅ Sentence translation (offline, via Argos Translate)

- ✅ Audio generation (via gTTS)

---

## 🛠 Example Output (Anki Card)

Front:

```text
さよなら より ずっと 大切 な
```

- Also displays furigana above the Kanji characters.
- `たいせつ` shall be displayed atop of the characters `大切`, for example, to clarify their pronunciation.

Back:

```text
サヨナラ ヨリ ズット タイセツ ナ

sayonara yori zutto taisetsu na

More important

さよなら (さようなら): farewell, adieu, goodbye, so long
より (より): than
ずっと (ずっと): continuously in some state (for a long time, distance), throughout, all along, the whole time, all the way
大切 (大切): important, necessary, indispensable
な (だ): dui (one of the trigrams of the I Ching: swamp, west)
```

- Katakana pronunciation
- Romaji pronunciation
- Sentence Translation
- Word-wise meanings

---

## 🧠 Tech Stack

- `fugashi`: MeCab wrapper for tokenization

- `jamdict`: Japanese dictionary lookup

- `genanki`: Programmatic Anki deck builder

- `typer`: Beautiful Python CLI

- `rich`: CLI spinner/loader

- `jaconv`: Japanese Converter (interconverter for Hiragana, Katakana and more)

- `argostranslate`: Sentence Translation

- `gtts`: Generate audio from text (Text-to-Speech)

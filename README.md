# 🎵 jlyric2anki *(In-Progress)*

A CLI tool that converts Japanese song lyrics (in Kanji) into **Anki flashcards** for sentence mining and vocabulary learning.

---

## ✨ Features

- 🧠 Sentence-level mining from Japanese lyrics
- 📖 Auto-generates furigana, romaji, and word meanings
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
│ |── utils.py # Loader function (rich spinner)
| |── translator.py # Sentence Translation
| └── style.css # Styling for Anki template
├── tests/
│ ├── test_analyzer.py # Test cases for analyzer.py
│ |── test_utils.py # Test cases for utils.py
| └── test_translator.py
├── cli.py # CLI entry point using Typer
├── lyrics.txt # Input: Japanese lyrics (Kanji)
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

## 🛠 Example Output (Anki Card)

Front:

```scss
                  たいせつ
さよなら より ずっと 大切 な
```

Back:

```scss
サヨナラ ヨリ ズット タイセツ ナ

sayonara yori zutto taisetsu na

さよなら (さようなら): farewell, adieu, goodbye, so long
より (より): than
ずっと (ずっと): continuously in some state (for a long time, distance), throughout, all along, the whole time, all the way
大切 (大切): important, necessary, indispensable
な (だ): dui (one of the trigrams of the I Ching: swamp, west)
```

---

## 🧾 TODO (Coming Soon)

- Add audio support using TTS

---

## 🧠 Tech Stack

- `fugashi`: MeCab wrapper for tokenization

- `jamdict`: Japanese dictionary lookup

- `genanki`: Programmatic Anki deck builder

- `typer`: Beautiful Python CLI

- `rich`: CLI spinner/loader

- `jaconv`: Japanese Converter (interconverter for Hiragana, Katakana and more)

- `argostranslate`: Sentence Translation

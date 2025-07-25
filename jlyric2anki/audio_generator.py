from gtts import gTTS
from pathlib import Path


def generate_audio(sentence: str, output_dir: Path, index: int) -> str:
    output_dir.mkdir(parents=True, exist_ok=True)
    tts = gTTS(text=sentence, lang="ja")
    filename = str(output_dir / f"line_{index}.mp3")
    tts.save(filename)
    return filename

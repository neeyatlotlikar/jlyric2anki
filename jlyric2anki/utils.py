import re

from rich.progress import Progress, SpinnerColumn, TextColumn


def show_loader(task_description: str, func, *args, **kwargs):
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task(task_description, start=False)
        progress.start_task(task)
        result = func(*args, **kwargs)
        progress.update(task, completed=100)
    return result


def find_japanese(text):
    # Regex pattern for Hiragana, Katakana, and Kanji (CJK Ideographs)
    japanese_pattern = re.compile(r"[\u3040-\u30FF\u4E00-\u9FFF]")
    return japanese_pattern.findall(text)


def is_japanese(text):
    # Check if the text contains any Japanese characters
    return bool(find_japanese(text))


def find_kanji(text):
    # Regex pattern for Kanji (CJK Ideographs)
    kanji_pattern = re.compile(r"[\u4E00-\u9FFF]")
    return kanji_pattern.findall(text)


def is_kanji(text):
    # Check if the text contains any Kanji characters
    return bool(find_kanji(text))


def find_kana(text):
    # Regex pattern for Hiragana and Katakana
    kana_pattern = re.compile(r"[\u3040-\u30FF]")
    return kana_pattern.findall(text)


def is_kana(text):
    # Check if the text contains any Kana characters
    return bool(find_kana(text))


def find_hiragana(text):
    # Regex pattern for Hiragana
    hiragana_pattern = re.compile(r"[\u3040-\u30FF]")
    return hiragana_pattern.findall(text)


def is_hiragana(text):
    # Check if the text contains any Hiragana characters
    return bool(find_hiragana(text))


def find_katakana(text):
    # Regex pattern for Katakana
    katakana_pattern = re.compile(r"[\u30A0-\u30FF]")
    return katakana_pattern.findall(text)


def is_katakana(text):
    # Check if the text contains any Katakana characters
    return bool(find_katakana(text))

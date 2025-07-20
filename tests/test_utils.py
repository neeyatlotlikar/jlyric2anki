from jlyric2anki.utils import is_japanese, is_kanji, is_kana, is_hiragana, is_katakana


def test_is_japanese():
    assert is_japanese("こんにちは")  # Hiragana
    assert is_japanese("カタカナ")  # Katakana
    assert is_japanese("漢字")  # Kanji
    assert not is_japanese("Hello")  # English text
    assert not is_japanese("12345")  # Numeric text


def test_is_kanji():
    assert is_kanji("漢字")  # Kanji
    assert not is_kanji("こんにちは")  # Hiragana
    assert not is_kanji("カタカナ")  # Katakana
    assert not is_kanji("Hello")  # English text
    assert not is_kanji("12345")  # Numeric text


def test_is_kana():
    assert is_kana("こんにちは")  # Hiragana
    assert is_kana("カタカナ")  # Katakana
    assert not is_kana("漢字")  # Kanji
    assert not is_kana("Hello")  # English text
    assert not is_kana("12345")  # Numeric text


def test_is_hiragana():
    assert is_hiragana("こんにちは")  # Hiragana
    assert not is_hiragana("カタカナ")  # Katakana
    assert not is_hiragana("漢字")  # Kanji
    assert not is_hiragana("Hello")  # English text
    assert not is_hiragana("12345")  # Numeric text


def test_is_katakana():
    assert is_katakana("カタカナ")  # Katakana
    assert not is_katakana("こんにちは")  # Hiragana
    assert not is_katakana("漢字")  # Kanji
    assert not is_katakana("Hello")  # English text
    assert not is_katakana("12345")  # Numeric text

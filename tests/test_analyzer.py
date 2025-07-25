from jlyric2anki.analyzer import analyze_line
from jlyric2anki.utils import is_japanese, is_katakana


def test_analyze_line():
    # Test with a simple line
    # initialize a line with a japanese sentence
    line = "こんにちは、世界！ This is a test line."
    result = analyze_line(line)
    print(result)  # For debugging purposes
    assert isinstance(result, dict)
    # Check if the result contains expected keys
    assert "kanji" in result
    assert "pronunciation" in result
    assert "romaji" in result
    assert "meanings" in result
    # Check if the values are of expected types
    assert isinstance(result["kanji"], str)
    assert isinstance(result["pronunciation"], str)
    assert isinstance(result["romaji"], str)
    assert isinstance(result["meanings"], str)
    # Check if the kanji, pronunciation, romaji, and meanings are not empty
    assert result["pronunciation"] != ""
    assert result["romaji"] != ""
    assert result["meanings"] != ""
    # Check if the kanji contains ruby tags
    assert "<ruby>" in result["kanji"]
    # Check if the pronunciation contains only katakana characters
    assert is_katakana(result["pronunciation"])
    # Check if the romaji does not contain Japanese characters
    assert not is_japanese(result["romaji"])

    # Test with an empty line
    line = ""
    result = analyze_line(line)
    print(result)  # For debugging purposes
    assert isinstance(result, dict)
    # Check if the result contains expected keys
    assert "kanji" in result
    assert "pronunciation" in result
    assert "romaji" in result
    assert "meanings" in result
    # Check if the values are of expected types
    assert isinstance(result["kanji"], str)
    assert isinstance(result["pronunciation"], str)
    assert isinstance(result["romaji"], str)
    assert isinstance(result["meanings"], str)
    # Check if the kanji, pronunciation, romaji, and meanings are empty
    assert result["kanji"] == ""
    assert result["pronunciation"] == ""
    assert result["romaji"] == ""
    assert result["meanings"] == "<br><br>"

    # Test with a line containing special characters
    line = "Hello, world! @2023"
    result = analyze_line(line)
    print(result)  # For debugging purposes
    assert isinstance(result, dict)
    # Check if the result contains expected keys
    assert "kanji" in result
    assert "pronunciation" in result
    assert "romaji" in result
    assert "meanings" in result
    # Check if the values are of expected types
    assert isinstance(result["kanji"], str)
    assert isinstance(result["pronunciation"], str)
    assert isinstance(result["romaji"], str)
    assert isinstance(result["meanings"], str)

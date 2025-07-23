from jlyric2anki.translator import translate_sentence


def test_translate_sentence():
    # Test basic translation
    result = translate_sentence("こんにちは", from_code="ja", to_code="en")
    assert result == "Hello!"

    # Test edge case with an English sentence
    result = translate_sentence("Hello", from_code="ja", to_code="en")
    print(result)
    assert result

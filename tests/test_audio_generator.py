from jlyric2anki.audio_generator import generate_audio


def test_generate_audio(tmp_path):
    sentence = "こんにちは"
    output_dir = tmp_path / "audio"
    index = 0

    # Call the function to generate audio
    audio_file = generate_audio(sentence, output_dir, index)

    # Check if the audio file was created
    generated_file = output_dir / f"line_{index}.mp3"
    assert audio_file == str(generated_file)
    assert generated_file.exists()
    assert generated_file.stat().st_size > 0

from argostranslate import package, translate


def setup_argos_translate(from_code="ja", to_code="en"):
    available_packages = package.get_available_packages()
    pkg = next(
        (
            p
            for p in available_packages
            if p.from_code == from_code and p.to_code == to_code
        ),
        None,
    )
    if pkg:
        package.install_from_path(pkg.download())


def translate_sentence(sentence: str, from_code="ja", to_code="en") -> str:
    installed_languages = translate.get_installed_languages()
    from_lang = next(
        (lang for lang in installed_languages if lang.code == from_code), None
    )
    to_lang = next((lang for lang in installed_languages if lang.code == to_code), None)
    if from_lang and to_lang:
        translator = from_lang.get_translation(to_lang)
        return translator.translate(sentence)
    return "Translation unavailable"

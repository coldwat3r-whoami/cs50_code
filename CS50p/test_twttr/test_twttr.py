from twttr import shorten


def test_caps():
    assert shorten("twIttEr") == "twttr"


def test_twitter():
    assert shorten("Twitter") == "Twttr"


def test_check50():
    assert shorten("how are you?") == "hw r y?"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"

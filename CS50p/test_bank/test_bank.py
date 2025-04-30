from bank import value

def test_hello():
    assert value("hello") == 0


def test_starts_with_h():
    assert value("How you doin?") == 20
    assert value("howdy!") == 20


def test_wrong_greeting():
    assert value("What's up!") == 100
    assert value("Yo!") == 100

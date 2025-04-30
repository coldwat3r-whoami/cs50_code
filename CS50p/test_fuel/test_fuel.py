from fuel import convert, gauge

def test_convert_output():
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    assert convert("0/4") == 0

def test_convert_errors():
    try:
        convert("4/0")
    except ZeroDivisionError:
        pass
    else:
        assert False

    try:
        convert("three/four")
    except ValueError:
        pass
    else:
        assert False

    try:
        convert("5/4")
    except ValueError:
        pass
    else:
        assert False

def test_gauge_output():
    assert gauge(75) == "75%"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(25) == "25%"

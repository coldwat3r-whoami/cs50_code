from plates import is_valid

def test_incorrect_length():
    assert is_valid("CS") == True
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False

def test_middle_zero():
    assert is_valid("CS05") == False

def test_starts_with_numbers():
    assert is_valid("50CS50p") == False
    assert is_valid("305786") == False

def test_letters_after_numbers():
    assert is_valid("CS50P") == False

def test_special_characters():
    assert is_valid("PI3.14") == False

def test_valid_plate():
    assert is_valid("CS50") == True

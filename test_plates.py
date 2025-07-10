from plates import is_valid

def test_length():
    # This test verifies the length constraints.
    # Plates must be between 2 and 6 characters, inclusive.
    assert is_valid("A") == False  # Too short
    assert is_valid("OUTATIME") == False # Too long
    assert is_valid("CS50") == True # Valid length
    assert is_valid("H") == False # Too short


def test_starting_letters():
    # This test ensures that every plate starts with at least two letters.
    assert is_valid("CS") == True
    assert is_valid("C5") == False # First two must be letters
    assert is_valid("50") == False # First two must be letters
    assert is_valid("A9") == False # First two must be letters


def test_number_rules():
    # This test checks the rules for using numbers in a plate.
    # - The first number cannot be '0'.
    # - Numbers must only appear at the end, not in the middle.
    assert is_valid("CS05") == False # First number can't be '0'
    assert is_valid("CS50P") == False # Numbers can't be in the middle
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False # Numbers can't be in the middle


def test_invalid_characters():
    # This test checks for any invalid characters, like punctuation or spaces.
    # Only alphanumeric characters are allowed.
    assert is_valid("CS50.") == False
    assert is_valid("CS 50") == False
    assert is_valid("PI3.14") == False

def test_all_letters():
    # This test checks for plates that contain only letters, which should be valid
    # as long as they meet the length requirement.
    assert is_valid("HELLO") == True
    assert is_valid("GOODBYE") == False # Too long
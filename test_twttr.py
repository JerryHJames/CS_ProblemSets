from twttr import shorten


def test_shorten_removes_lowercase_vowels():
    assert shorten("aeiou") == ""


def test_shorten_removes_uppercase_vowels():
    assert shorten("AEIOU") == ""


def test_shorten_mixed_string():
    assert shorten("Hello, World!") == "Hll, Wrld!"


def test_shorten_no_vowels():
    assert shorten("bcdfg") == "bcdfg"


def test_shorten_empty_string():
    assert shorten("") == ""


def test_shorten_numbers_and_punctuation():
    assert shorten("1234!@#$") == "1234!@#$"


def test_shorten_word_with_vowels_and_consonants():
    assert shorten("Python") == "Pythn"

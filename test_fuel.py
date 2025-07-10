import pytest
# We need to import our functions from fuel.py to test them.
from fuel import convert, gauge

def test_convert_valid_fractions():
    # This test ensures that the convert function correctly processes
    # valid fraction strings and returns the expected integer percentage.
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("99/100") == 99
    assert convert("1/100") == 1


def test_convert_invalid_input():
    # This test checks that the convert function raises a ValueError
    # when given improperly formatted strings or when the numerator
    # is larger than the denominator.
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ValueError):
        convert("1.5/3")


def test_convert_negative_fraction():
    # This test checks that a ValueError is raised for negative fractions.
    with pytest.raises(ValueError):
        convert("-1/4")
    with pytest.raises(ValueError):
        convert("1/-4")


def test_convert_zero_division():
    # This test specifically checks that a ZeroDivisionError is raised
    # when the denominator of the fraction is zero.
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge_output():
    # This test verifies that the gauge function returns the correct
    # string representation for different percentage levels.
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
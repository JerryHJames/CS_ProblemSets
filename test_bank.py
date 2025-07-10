from bank import value

def test_hello():
    # Greetings that start with "hello" should return 0 dollars.
    assert value("hello") == 0
    assert value("Hello, Newman") == 0
    assert value("HELLO WORLD") == 0


def test_starts_with_h():
    # Greetings starting with "h" but not exactly "hello" should return 20 dollars.
    assert value("h") == 20
    assert value("How you doing?") == 20
    assert value("Hey") == 20

def test_other_greetings():
    assert value("What's happening?") == 100
    assert value("Good morning") == 100
    assert value("   sup") == 100

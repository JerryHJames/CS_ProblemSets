import random

def get_level():
    # Keep asking until the player gives us a positive integer for difficulty
    while True:
        level = input("Level: ")
        if level.isdigit() and int(level) > 0:
            return int(level)
        # If we reach here, the input wasn't a valid positive integer—ask again

def get_guess():
    # Keep asking until the player enters a positive integer guess
    while True:
        guess = input("Guess: ")
        if guess.isdigit() and int(guess) > 0:
            return int(guess)
        # Invalid guess; prompt again

def main():
    # Determine the upper bound for our secret number
    level = get_level()

    # Pick a random secret number between 1 and level, inclusive
    secret = random.randint(1, level)

    # Let the guessing begin
    while True:
        guess = get_guess()
        if guess < secret:
            print("Too small!")
        elif guess > secret:
            print("Too large!")
        else:
            print("Just right!")
            break  # Exit once the correct guess is made
main()

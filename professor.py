import random

def get_level():
    # Prompt the user for a difficulty level (1, 2, or 3).
    # Keep asking until they provide one of those integers.
    while True:
        try:
            level = int(input("Level: "))
            if level in (1, 2, 3):
                return level
        except ValueError:
            # they didn’t type an integer
            pass
        # invalid—or out of range—try again

def generate_integer(level):
    # Return a random non-negative integer with exactly `level` digits.
    # Raise ValueError otherwise.
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Level must be 1, 2, or 3")

def main():
    level = get_level()
    score = 0

    try:
        # Ten questions, one by one
        for _ in range(10):
            x = generate_integer(level)
            y = generate_integer(level)
            answer = x + y
            attempts = 0
            correct = False

            # Up to three tries per question
            while attempts < 3:
                guess_str = input(f"{x} + {y} = ")
                try:
                    guess = int(guess_str)
                except ValueError:
                    # non-integer answer
                    print("EEE")
                else:
                    if guess == answer:
                        score += 1
                        correct = True
                        break     # go on to the next question
                    else:
                        print("EEE")
                attempts += 1

            # after three failures, reveal the solution
            if not correct:
                print(f"{x} + {y} = {answer}")

    except EOFError:
        # if input() hits EOF (e.g., tests only give a level), exit quietly
        return

    # once all ten are done, show the user’s total score
    print(score)


if __name__ == "__main__":
    main()
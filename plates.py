def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # First, let's check the length constraint.
    if not 2 <= len(s) <= 6:
        return False

    # The plate must be composed of only letters and numbers.
    if not s.isalnum():
        return False

    # The first two characters absolutely must be letters.
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Now, we'll handle the rules about numbers.
    # We need to find where the numbers start.
    first_number_found = False
    for char in s:
        if char.isdigit():
            # If we find a digit, this is the start of the number sequence.
            # The first number cannot be '0'.
            if not first_number_found and char == '0':
                return False
            first_number_found = True
        elif first_number_found:
            # If we've already found a number, any subsequent character
            # that is a letter is a violation of the rule.
            return False

    # If the plate has passed all these checks, it's valid.
    return True


if __name__ == "__main__":
    main()

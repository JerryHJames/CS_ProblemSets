def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check that the length of the letters is between 2 - 6 chars
    if len(s) < 2 or len(s) > 6:
        return False

    # Check that it starts with at least 2 letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Check for invalid Chars
    for char in s:
        if not char.isalnum():
            return False

    # Check the number placement
    found_number = False
    for i, char in enumerate(s):
        if char.isdigit():
            # First number can't be 0
            if not found_number and char == '0':
                return False
            found_number = True
        elif found_number:
            return False

    return True

if __name__ == "__main__":
    main()

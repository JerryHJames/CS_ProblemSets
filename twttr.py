def main():
    # Get some text from the user
    text = input("Input: ")

    # These are all the vowels we want to get rid of
    vowels = "aeiouAEIOU"

    # Start with an empty result string
    result = ""

    # Go through each character in the text
    for char in text:
        # If it's not a vowel, keep it
        if char not in vowels:
            result += char

    # Show the shortened version
    print(result)

if __name__ == "__main__":
    main()

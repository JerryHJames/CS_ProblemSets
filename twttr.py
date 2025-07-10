def main():
    # Prompt the user for input and print the shortened version.
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    # Return word but with all English vowels (uppercase and lowercase) removed.
    vowels = set("AEIOUaeiou")
    return "".join(char for char in word if char not in vowels)


if __name__ == "__main__":
    main()

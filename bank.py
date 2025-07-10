def main():

    # Prompt the user for a greeting and print the corresponding value.
    greeting = input("Greeting: ")
    # Calculate the value of the greeting using our value function.
    result = value(greeting)
    print(f"${result}")


def value(greeting):
    # To make our logic simpler, let's clean up the input string.
    # We'll convert it to lowercase and strip any leading whitespace.
    normalized_greeting = greeting.lower().strip()

    # Now, let's check the conditions.
    # If the greeting starts with "hello", the value is 0.
    if normalized_greeting.startswith("hello"):
        return 0
    # If it just starts with an "h", the value is 20.
    elif normalized_greeting.startswith("h"):
        return 20
    # For everything else, the value is 100.
    else:
        return 100

if __name__ == "__main__":
    main()

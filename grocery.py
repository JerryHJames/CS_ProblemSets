def main():
    # Dictionary to store the items and their counts
    grocery_list = {}

    # Keep asking for items until the user hits Ctrl-D
    while True:
        try:
            # Get the item from the user
            item = input().strip()
            # Skip empty lines
            if not item:
                continue
            # Convert to uppercase
            item_upper = item.upper()

            # Add to our grocery list or increment count if already exists
            # Use the .get() method to safely get the current count (0 if not found)
            grocery_list[item_upper] = grocery_list.get(item_upper, 0) + 1

        # Listen for user to hit Ctrl-D
        except EOFError:
            break
        # Sort the items in alpabetical order and print
    for item in sorted(grocery_list.keys()):
        count = grocery_list[item]
        print(f"{count} {item}")

if __name__ == "__main__":
    main()

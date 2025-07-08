def main():
    # Felipe's menu with prices
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    # Keep track of the running total
    total = 0.0

    # Keep asking the user for items until they hit Ctrl-D
    while True:
        try:
            # Get items from the user
            item = input("Item: ").strip()

            # Convert to title case to match the menu format
            item_formatted = item.title()

            # Check if the item is on the menu, add the price to our running total, and print the total.
            if item_formatted in menu:
                total += menu[item_formatted]
                print(f"Total: ${total:.2f}")

        except EOFError:
            # Exit once the user hits Ctrl-D
            print()
            break
main()


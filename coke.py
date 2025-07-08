def main():
    # A coke costs 50 cents
    price = 50

    # Only accepts these coins (no pennies)
    valid_coins = [25, 10,5]

    # Keep track of how much money we've gotten
    amount_paid = 0

    # Continue to ask the user for coins until they pay the amount due
    while amount_paid < price:
        # Calculate how much they owe
        amount_due = price - amount_paid

        # Ask for another coin
        coin = int(input("Insert Coin: "))

        # Only accept the correct coin
        if coin in valid_coins:
            # Add it to the total
            amount_paid += coin

        # If more is need, let the user know how much
        if amount_paid < price:
            amount_due = price - amount_paid
            print(f"Amount Due: {amount_due}")

    # If overpaid, give change
    change = amount_paid - price
    print(f"Change Owed: {change}")

if __name__ == "__main__":
    main()
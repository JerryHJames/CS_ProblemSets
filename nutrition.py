def main():
    # Get fruit name from user
    fruit = input("Item: ")

    # Dictionary of fruits and their calories per FDA serving size
    # Data from FDA Raw Fruits Poster (Text Version)
    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }

    # Convert input to lowercase for case-insensitive comparison
    fruit_lower = fruit.lower()

    # Check if the fruit is in our database
    if fruit_lower in fruits:
        calories = fruits[fruit_lower]
        print(f"Calories: {calories}")
    # If fruit not found, output nothing (ignore invalid input)
main()

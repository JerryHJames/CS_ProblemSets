def main():
    response = input("Greeting: ").strip().lower()
    print(value(response))

# Find out the value of the response
def value(response):
    if response.startswith("hello"):
        return "$0"
    elif response.startswith("h"):
        return "$20"
    else:
        return "$100"

main()

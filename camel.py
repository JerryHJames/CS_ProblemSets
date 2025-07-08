def main():
    camel_input = input("camelCase: ")
    snake_output = convert_to_snake(camel_input)
    print(f"snake_case: {snake_output}")

def convert_to_snake(camel_str):
    snake_parts = []
    for char in camel_str:
        if char.isupper():
            snake_parts.append("_" + char.lower())
        else:
            snake_parts.append(char)
    return "".join(snake_parts)

if __name__ == "__main__":
    main()
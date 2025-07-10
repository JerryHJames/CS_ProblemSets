import sys

def main():
    # Validate command-line arguments.
    check_arguments()

    # Process the file specified by the user.
    try:
        file_path = sys.argv[1]
        line_count = count_lines_in_file(file_path)
        print(line_count)
    except FileNotFoundError:
        # Exit if file not found.
        sys.exit("File does not exist")


def check_arguments():
    # Check argument count.
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Check for .py extension.
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")


def count_lines_in_file(file_path):
    # Initialize line counter.
    code_lines = 0
    # Open and read the file.
    with open(file_path, "r") as file:
        for line in file:
            # Remove leading whitespace.
            stripped_line = line.lstrip()

            # Skip blank lines and comments.
            if stripped_line.startswith("#") or stripped_line == "":
                continue

            # Increment code line counter.
            code_lines += 1
    return code_lines

if __name__ == "__main__":
    main()
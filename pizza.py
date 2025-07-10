import sys
import csv
from tabulate import tabulate

def main():
    # Validate command-line arguments.
    check_arguments()

    # Try to read and format the specified CSV file.
    try:
        file_path = sys.argv[1]
        formatted_menu = read_and_format_menu(file_path)
        print(formatted_menu)
    except FileNotFoundError:
        # Exit if the file doesn't exist.
        sys.exit("File does not exist")

def check_arguments():
    # Check for the correct number of arguments.
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Ensure the file is a CSV.
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

def read_and_format_menu(file_path):
    # Read the menu data from the CSV.
    menu_items = []
    with open(file_path) as file:
        reader = csv.reader(file)
        for row in reader:
            menu_items.append(row)

    # Format the data into a grid table using tabulate.
    return tabulate(menu_items, headers="firstrow", tablefmt="grid")

if __name__ == "__main__":
    main()

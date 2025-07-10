import sys
import csv

def main():
    # Validate command-line arguments.
    check_arguments()

    # Define input and output file paths.
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Process the input file and write to the output file.
    try:
        clean_csv_data(input_file, output_file)
    except FileNotFoundError:
        # Exit if the input file can't be read.
        sys.exit(f"Could not read {input_file}")

def check_arguments():
    # Check for the correct number of arguments.
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

def clean_csv_data(input_path, output_path):
    # A list to store the cleaned student data.
    cleaned_rows = []
    # Read the data from the input file.
    with open(input_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Split the name into last and first.
            last, first = row["name"].split(", ")
            # Add the cleaned data to our list.
            cleaned_rows.append({"first": first, "last": last, "house": row["house"]})

    # Write the cleaned data to the output file.
    with open(output_path, "w", newline="") as file:
        # Define the header for the new CSV.
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        # Write the header row.
        writer.writeheader()
        # Write the cleaned student data.
        writer.writerows(cleaned_rows)

if __name__ == "__main__":
    main()
import sys
import inflect

def main():
    # Initialize the inflect engine to format lists with commas and "and"
    engine = inflect.engine()

    # Read all input lines (one name per line) until the user signals EOF (Ctrl+D)
    input_lines = sys.stdin.read().splitlines()

    # Filter out any blank or whitespace-only lines
    names = [line for line in input_lines if line.strip()]

    # Convert ["Alice", "Bob", "Charlie"] into "Alice, Bob, and Charlie"
    formatted_names = engine.join(names)

    # Output the farewell message
    print(f"Adieu, adieu, to {formatted_names}")
main()

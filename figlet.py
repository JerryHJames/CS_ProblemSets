import random
import sys
from pyfiglet import Figlet

def main():
    # Create Figlet
    figlet = Figlet()
    # Get the list of fonts
    available_fonts = figlet.getFonts()

    # Check the number of command line args
    if len(sys.argv) == 1:
        # No arguments - Use random font
        font = random.choice(available_fonts)
        figlet.setFont(font=font)
    elif len(sys.argv) == 3:
        # Two args - Check if the first is -f or --font
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid usage")

        # Check if the second arg is a valid font
        font_name = sys.argv[2]
        if font_name not in available_fonts:
            sys.exit("Invalid usage")

        figlet.setFont(font=font_name)
    else:
        # Wrong number of args
        sys.exit("Invalid usage")

    # Get text from the user
    text = input("Input: ")

    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
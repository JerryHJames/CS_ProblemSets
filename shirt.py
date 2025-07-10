import sys
import os
from PIL import Image, ImageOps

def main():
    # Validate command-line arguments.
    check_arguments()

    # Define input and output file paths.
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Process the image, handling file errors.
    try:
        overlay_shirt(input_path, output_path)
    except FileNotFoundError:
        # Exit if the input file doesn't exist.
        sys.exit("Input does not exist")

def check_arguments():
    # Check for the correct number of arguments.
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Define valid file extensions.
    valid_extensions = [".jpg", ".jpeg", ".png"]
    # Get extensions from file paths, ensuring case-insensitivity.
    input_ext = os.path.splitext(sys.argv[1])[1].lower()
    output_ext = os.path.splitext(sys.argv[2])[1].lower()

    # Check if file extensions are valid.
    if input_ext not in valid_extensions:
        sys.exit("Invalid input")
    if output_ext not in valid_extensions:
        sys.exit("Invalid output")

    # Check if input and output extensions match.
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

def overlay_shirt(input_path, output_path):
    # Open the base shirt and input photo images.
    shirt = Image.open("shirt.png")
    photo = Image.open(input_path)

    # Get the size of the shirt image for fitting.
    shirt_size = shirt.size

    # Resize and crop the photo to match the shirt's dimensions.
    photo_fitted = ImageOps.fit(photo, shirt_size)

    # Paste the shirt onto the fitted photo, using the shirt's alpha channel as a mask.
    photo_fitted.paste(shirt, shirt)

    # Save the final composed image.
    photo_fitted.save(output_path)

if __name__ == "__main__":
    main()
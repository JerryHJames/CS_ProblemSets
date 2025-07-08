# Define main function
def main():
    # Ask the user for a file name
    file_name = input("File name: ").strip().lower()
    # Print the media type
    print(media_type(file_name))


#Output the file media type based on suffix
def media_type(file_name):
    if file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
        return "image/jpeg"
    elif file_name.endswith(".gif"):
        return "image/gif"
    elif file_name.endswith(".png"):
        return "image/png"
    elif file_name.endswith("pdf"):
        return "application/pdf"
    elif file_name.endswith(".txt"):
        return "text/plain"
    elif file_name.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

main()

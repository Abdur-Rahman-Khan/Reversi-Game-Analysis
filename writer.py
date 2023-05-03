def write_file(file_name, content):
    with open(file_name, "a+") as file:
        # Go to the beginning of the file
        file.seek(0)
        # Check if the file is empty
        if not file.read():
            # If the file is empty, write some initial content
            file.write(content)
        # Append some new content to the file
        else:
            file.write(content)

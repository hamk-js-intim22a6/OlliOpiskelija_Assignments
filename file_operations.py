def load_text_file(path):
    """
    Load the contents of a text file.

    Args:
        path (str): The path to the text file.

    Returns:
        str: The contents of the text file.

    Raises:
        FileNotFoundError: If the file is not found.
        IOError: If there is an error reading the file.
    """
    try:
        with open(path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except IOError:
        print(f"Error: Unable to read file '{path}'.")
        return None

def save_text_file(path, text):
    """
    Save the contents to a text file.

    Args:
        path (str): The path to the text file.
        text (str): The contents to be saved.

    Raises:
        IOError: If there is an error writing to the file.
    """
    try:
        with open(path, 'w') as file:
            file.write(text)
    except IOError:
        print(f"Error: Unable to write to file '{path}'.")

def load_binary_file(path):
    """
    Load the contents of a binary file.

    Args:
        path (str): The path to the binary file.

    Returns:
        bytes: The contents of the binary file.

    Raises:
        FileNotFoundError: If the file is not found.
        IOError: If there is an error reading the file.
    """
    try:
        with open(path, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except IOError:
        print(f"Error: Unable to read file '{path}'.")
        return None

def save_binary_file(path, data):
    """
    Save the contents to a binary file.

    Args:
        path (str): The path to the binary file.
        data (bytes): The contents to be saved.

    Raises:
        IOError: If there is an error writing to the file.
    """
    try:
        with open(path, 'wb') as file:
            file.write(data)
    except IOError:
        print(f"Error: Unable to write to file '{path}'.")

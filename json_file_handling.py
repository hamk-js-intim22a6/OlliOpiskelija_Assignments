import json

def load_dictionary(path):
    """
    Load a dictionary from a JSON file.

    Args:
        path (str): The path to the JSON file.

    Returns:
        dict: The loaded dictionary.
        none: If the file does not exist or is not a valid JSON.
    """
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except IOError:
        print(f"Error: Unable to read file '{path}'.")
        return None
    except json.JSONDecodeError as e:
        print(f"Corrupted dictionary file. Error: Invalid JSON file '{path}: {e}'.")
        return None
    
def save_dictionary(d, path):
    """
    Save a dictionary to a JSON file.

    Args:
        d (dict): The dictionary to save.
        path (str): The path to the JSON file.

    Returns:
        bool: True if the dictionary was saved successfully, False otherwise.

    Example:
        d = {"cat": "kissa", "dog": "koira"}
        path = "dictionary.json"
        save_dictionary(d, path)
    """
    try:
        with open(path, 'w') as f:
            json.dump(d, f)
            return True
    except IOError:
        print(f"Error: Unable to write to file '{path}'.")
        return False

def main():
    #d = {"cat": "kissa", "dog": "koira"}
    #path = "dictionary.json"
    #save_dictionary(d, path)
    #del d
    d = load_dictionary("dictionary.json")
    if d:
        for word, translation in d.items():
            print(f"{word} = {translation}")
    else:
        print("Failed to load the dictionary.")

if __name__ == "__main__":
    main()

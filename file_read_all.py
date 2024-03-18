try:
    with open("testix.txt", "r") as f:
        data = f.read()
        print(data, end="")
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("Error reading the file.")

# The with statement is used to open the file. The file is closed automatically when the block ends.

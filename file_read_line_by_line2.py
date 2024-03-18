with open("testi.txt", "r") as f:
    data = f.readlines()
    for line in data:
        print(line, end="")
# The with statement is used to open the file. The file is closed automatically when the block ends.
        
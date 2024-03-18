try:
    with open("testi.txt", "w") as f:
        f.write("Hei tämä on esimerkki\n")
        x = input("Kirjoita jotain: ")
        f.flush()
        f.write("Tämä on toinen rivi\n")
        x = input("Kirjoita jotain #2: ")
except IOError as e:
    print("Error: Failed to write to file -", str(e))
# The with statement is used to open the file. The file is closed automatically when the block ends.

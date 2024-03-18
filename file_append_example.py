try:
    with open("non_existing_folder/testix.txt", "a") as f:
        f.write("Tämä lisätään tekstitiedoston loppuun\n")
except IOError as e:
    print("An error occurred trying to write to file:", str(e))

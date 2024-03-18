d = {"cat": "kissa", "dog": "koira"}
while True:
    word = input("Enter a word: ")
    if not word:
        print("Bye!")
        break  # If the user enters an empty string, the program stops
    if word in d:
        print(f"{word} = {d[word]}") # If the word is found in the dictionary, the program prints the word and its translation
    else:
        definition = input(f"Unknown word. Enter the translation for {word}: ")
        if definition:
            d[word] = definition # adds the word and its translation to the dictionary
            print(f"{word} = {definition} added to dictionary")

import tkinter as tk
from googletrans import Translator, LANGUAGES

def translate_text():
    try:
        text_to_translate = translator.translate(text=word_entry.get(), src=source_language.get(), dest=destination_language.get())
        translation_text.set(text_to_translate.text)
    except Exception as e:
        translation_text.set("Error: " + str(e))

# Main window
root = tk.Tk()
root.title("Language Learning App")

# Translator
translator = Translator()

# Language options
language_options = list(LANGUAGES.values())

# Variables
source_language = tk.StringVar(root)
destination_language = tk.StringVar(root)
translation_text = tk.StringVar(root)

# Default languages
source_language.set('english')
destination_language.set('spanish')

# UI Elements
word_entry = tk.Entry(root)
word_entry.grid(row=0, column=1, padx=10, pady=10)

source_language_menu = tk.OptionMenu(root, source_language, *language_options)
source_language_menu.grid(row=1, column=1, padx=10, pady=10)

destination_language_menu = tk.OptionMenu(root, destination_language, *language_options)
destination_language_menu.grid(row=1, column=2, padx=10, pady=10)

translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.grid(row=2, column=1, padx=10, pady=10)

translation_label = tk.Label(root, textvar=translation_text, bg='light yellow', wraplength=300)
translation_label.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

# Main loop
root.mainloop()

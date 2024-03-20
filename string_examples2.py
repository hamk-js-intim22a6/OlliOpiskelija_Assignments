import string

# Example 1: Accessing ASCII lowercase letters
print(string.ascii_lowercase)

# Example 2: Accessing ASCII uppercase letters
print(string.ascii_uppercase)

# Example 3: Accessing ASCII letters (both lowercase and uppercase)
print(string.ascii_letters)

# Example 4: Accessing digits
print(string.digits)

# Example 5: Accessing hexadecimal digits
print(string.hexdigits)

# Example 6: Accessing octal digits
print(string.octdigits)

# Example 7: Accessing punctuation characters
print(string.punctuation)

# Example 8: Accessing whitespace characters
print(string.whitespace)

# Example 9: Creating a translation table for string translation
trans_table = str.maketrans("aeiou", "12345")
translated = "This is an example.".translate(trans_table)
print(translated)

# Example 10: Removing punctuation from a string
import re
sample_text = "Hello, World! This is an example."
clean_text = re.sub(f"[{string.punctuation}]", "", sample_text)
print(clean_text)

# Example 11: Checking if a character is a letter
def is_letter(char):
    return char in string.ascii_letters

print(is_letter("a"))  # True
print(is_letter("1"))  # False

# Example 12: Checking if a string contains only letters
def contains_only_letters(test_string):
    return all(char in string.ascii_letters for char in test_string)

print(contains_only_letters("Hello"))  # True
print(contains_only_letters("Hello123"))  # False

# Example 13: Generating a random password with letters and digits
import random
def generate_password(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

print(generate_password(10))

# Example 14: Checking if a string contains any punctuation
def contains_punctuation(test_string):
    return any(char in string.punctuation for char in test_string)

print(contains_punctuation("Hello!"))  # True
print(contains_punctuation("Hello"))  # False

# Example 15: Splitting a string while ignoring whitespace
def split_ignore_whitespace(test_string):
    return re.split(r"\S+", test_string)

print(split_ignore_whitespace("Hello   World!"))

# Example 16: Capitalizing each word in a string
def capitalize_each_word(s):
    return ' '.join(word.capitalize() for word in s.split())

print(capitalize_each_word("hello world"))

# Example 17: Creating a safe filename by removing punctuation
def create_safe_filename(filename):
    return re.sub(f"[{string.punctuation}]", "", filename)

print(create_safe_filename("my*file?.txt"))

# Example 18: Converting a string to a valid Python identifier
def to_identifier(input_string):
    return re.sub(r'\W|^(?=\d)', '_', input_string)

print(to_identifier("123abc def"))

# Example 19: Counting vowels in a string
def count_vowels(input_string):
    return sum(1 for char in input_string if char in "aeiouAEIOU")

print(count_vowels("Hello World"))

# Example 20: Removing digits from a string
def remove_digits(input_string):
    return input_string.translate(str.maketrans('', '', string.digits))

print(remove_digits("abc123def456"))

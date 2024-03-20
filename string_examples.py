# Example 1: Concatenating two strings
str1 = "Hello, "
str2 = "World!"
concatenated = str1 + str2
print(concatenated)

# Example 2: Converting to uppercase
upper_str = "hello".upper()
print(upper_str)

# Example 3: Converting to lowercase
lower_str = "HELLO".lower()
print(lower_str)

# Example 4: Checking if a string starts with a substring
starts_with_hello = "Hello World!".startswith("Hello")
print(starts_with_hello)

# Example 5: Checking if a string ends with a substring
ends_with_world = "Hello World!".endswith("World!")
print(ends_with_world)

# Example 6: Finding a substring within a string
index_of_world = "Hello World!".find("World")
print(index_of_world)

# Example 7: Replacing a substring with another substring
replaced_str = "Hello World!".replace("World", "Python")
print(replaced_str)

# Example 8: Stripping whitespace from the ends of a string
stripped_str = "   Hello World!   ".strip()
print(stripped_str)

# Example 9: Splitting a string into a list
split_str = "Hello,World,Python".split(",")
print(split_str)

# Example 10: Joining a list of strings into a single string
joined_str = "-".join(["Hello", "World", "Python"])
print(joined_str)

# Example 11: Checking if all characters in the string are alphanumeric
is_alnum = "Hello123".isalnum()
print(is_alnum)

# Example 12: Checking if all characters in the string are alphabetic
is_alpha = "Hello".isalpha()
print(is_alpha)

# Example 13: Checking if all characters in the string are digits
is_digit = "12345".isdigit()
print(is_digit)

# Example 14: Checking if the string is in title case
is_title = "Hello World".istitle()
print(is_title)

# Example 15: Checking if the string is in lowercase
is_lower = "hello world".islower()
print(is_lower)

# Example 16: Checking if the string is in uppercase
is_upper = "HELLO WORLD".isupper()
print(is_upper)

# Example 17: Converting a string into title case
title_str = "hello world".title()
print(title_str)

# Example 18: Padding a string with zeros
zfilled_str = "42".zfill(5)
print(zfilled_str)

# Example 19: Checking if all characters in the string are whitespace
is_space = "   ".isspace()
print(is_space)

# Example 20: Formatting a string
formatted_str = "Hello, {}".format("Python")
print(formatted_str)

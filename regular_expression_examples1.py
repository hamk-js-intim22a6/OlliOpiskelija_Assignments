import re

def is_zip_code(string):
    if re.match(r'^\d{5}$', string):
        return True
    else:
        return False

print("Is '12345' a zip code?", is_zip_code('12345'))  # Output: True
print("Is '1234' a zip code?", is_zip_code('1234'))  # Output: False

string = "I have 10 apples and -5 oranges"
integers = re.findall(r'-?\d+', string)
print(integers)  # Output: ['10', '-5']

search_result = re.search(r'(-?\d+)', string)
if search_result:
    print(f"""start index: {search_result.start()}
end index: {search_result.end()}
matched string: {search_result.group()}""")

matches = re.match(r'(\d{1,4})-(\d{1,10})', "050-1234567")
if matches:
    print(matches.group(), matches.group(1), matches.group(2))

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False

email = "example@example.dot.com"
if is_valid_email(email):
    print("Valid email address")
else:
    print("Invalid email address")

def remove_html_tags(string):
    pattern = r'<.*?>'  # Non-greedy pattern to match HTML tags
    return re.sub(pattern, '', string)

html_string = "<body><h1>Title</h1>\n<p>This is a <b>bold</b> statement.</p></body>"
clean_string = remove_html_tags(html_string)
print(clean_string)  # Output: "Title\nThis is a bold statement."

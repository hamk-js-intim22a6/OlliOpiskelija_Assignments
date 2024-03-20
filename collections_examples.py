# Example 1: Using Counter to count word frequency

from collections import Counter

text = "This is a sample text to count word frequency. How often does each word appear?"
word_counts = Counter(text.lower().split())  # Convert to lowercase and split

print("Word frequency:")
for word, count in word_counts.items():
    print(f"{word}: {count}")


# Example 2: Using namedtuple to define custom data structures

from collections import namedtuple

# Define a namedtuple for Book details
Book = namedtuple("Book", ["title", "author", "year"])

# Create Book instances
book1 = Book(title="Pride and Prejudice", author="Jane Austen", year=1813)
book2 = Book(title="The Lord of the Rings", author="J.R.R. Tolkien", year=1954)

print(f"Book 1 details: {book1}")
print(f"Book 2 author: {book2.author}")  # Access by attribute


# Example 3: Using OrderedDict to maintain insertion order

from collections import OrderedDict

access_log = OrderedDict()
access_log["/home"] = 10
access_log["/about"] = 5
access_log["/contact"] = 2

print("Access log (insertion order preserved):")
for url, count in access_log.items():
    print(f"{url}: {count}")


# Example 4: Using defaultdict to provide default values

from collections import defaultdict

user_data = defaultdict(list)  # Default value is an empty list

user_data["Alice"].append("history")
user_data["Alice"].append("math")
user_data["Bob"].append("computer science")

print("User data (default list for missing keys):")
for user, courses in user_data.items():
    print(f"{user}: {courses}")


# Example 5: Using deque for efficient append/popleft

from collections import deque

recent_searches = deque(maxlen=5)  # Limit to 5 recent searches

recent_searches.append("shoes")
recent_searches.append("laptop")
recent_searches.append("phone")
recent_searches.append("headphones")

print(f"Recent searches (FIFO - oldest removed first): {recent_searches}")
print(f"Pop the oldest search: {recent_searches.popleft()}")
print(f"Recent searches after pop: {recent_searches}")


# Example 6: Using ChainMap to combine multiple dictionaries

from collections import ChainMap

defaults = {"username": "guest", "role": "user"}
user_settings = {"username": "alice"}

combined_settings = ChainMap(user_settings, defaults)

print(f"Combined settings (user overrides defaults): {combined_settings}")


# Example 7: Using UserDict for custom dictionary behavior

from collections import UserDict

class CaseInsensitiveDict(UserDict):
    def __getitem__(self, key):
        return super().__getitem__(key.lower())

    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)

# Create a case-insensitive dictionary
config = CaseInsensitiveDict()
config["ApiToken"] = "1234"

print(f"Access config key (case-insensitive): {config['apitoken']}")  # Works regardless of case


# Example 8: Using UserList for custom list behavior

from collections import UserList

class OrderedList(UserList):
    def append(self, item):
        # Insert at the end while maintaining order
        super().insert(len(self), item)

# Create an ordered list that appends to the end
ordered_list = OrderedList()
ordered_list.append(1)
ordered_list.append(3)
ordered_list.append(2)

print(f"Ordered list (appends maintain order): {ordered_list}")


# Example 9: Using namedtuple for custom data structures with methods

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

def distance(p1, p2):
    # Define a method within the namedtuple class
    return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5

pt1 = Point(1, 2)
pt2 = Point(4,

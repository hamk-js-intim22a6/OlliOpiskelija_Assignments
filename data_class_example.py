from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    city: str

# Create an instance of the Person class
person = Person("John Doe", 25, "New York")

# Access the attributes of the person object
print(person.name)  # Output: John Doe
print(person.age)   # Output: 25
print(person.city)  # Output: New York

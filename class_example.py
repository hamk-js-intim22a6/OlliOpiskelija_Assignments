class Person:
    """
    A class representing a person.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

    def __str__(self):
        return f"Person: {self.name}, {self.age}"


class Student(Person):
    """
    A class representing a student.

    Attributes:
        name (str): The name of the student.
        age (int): The age of the student.
        student_id (str): The ID of the student.
    """

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age}, student_id={self.student_id})"

    def __str__(self):
        return f"Student: {self.name}, {self.age}, ID: {self.student_id}"


def main():
    print("Class example Main function")
    # Create a Person object
    person = Person("John Doe", 25)
    print(person)  # Output: Person: John Doe, 25
    print(repr(person))  # Output: Person(name='John Doe', age=25)

    # Create a Student object
    student = Student("Jane Smith", 20, "12345")
    print(student)  # Output: Student: Jane Smith, 20, ID: 12345
    print(repr(student))  # Output: Student(name='Jane Smith', age=20, student_id=12345)


if __name__ == "__main__":
    main()

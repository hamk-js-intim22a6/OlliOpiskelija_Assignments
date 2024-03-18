#import class_example
#jill = class_example.Person("Jill", 25)
#print(jill)

from class_example import Person, Student

jill = Person("Jill", 25)
print(jill)
jill_student = Student("Jill", 25, "Computer Science")
print(jill_student)

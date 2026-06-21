# Creating Student class

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)


# Creating object
s1 = Student("Rahul", 85)

# Displaying details
s1.display()
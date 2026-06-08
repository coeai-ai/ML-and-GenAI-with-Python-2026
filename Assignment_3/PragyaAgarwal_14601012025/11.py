class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

name = input("Enter student name: ")
marks = float(input("Enter marks: "))

s1 = Student(name, marks)

s1.display()
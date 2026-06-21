class Student:
    def __init__(self, name, student_marks):
        self.name = name
        self.student_marks = student_marks

    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Marks:", self.student_marks)


name = input("Enter student name: ")
student_marks = input("Enter marks: ")

# Creating object
student = Student(name, student_marks)

# Displaying details
student.display()
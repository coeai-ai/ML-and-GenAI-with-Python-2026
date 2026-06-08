#1. Create a text file and store student details
file = open("students.txt", "w")
file.write("Name: Renaissance, Marks: 85\n")
file.write("Name: Ren, Marks: 92\n")
file.close()
#2. Read data from a file
file = open("students.txt", "r")
data = file.read()
print(data)
file.close()
#3. Handle division by zero using exception handling
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
#4. Create a Student class with name and marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
# Testing the Student class
s1 = Student("Renaissance", 55)
print("Student Name:", s1.name)
print("Student Marks:", s1.marks)
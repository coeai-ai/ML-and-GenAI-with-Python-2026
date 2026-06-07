#Create a function to print first 10 natural numbers.
def print_natural_numbers(n):
    for i in range(1, n + 1):
        print(i, end=' ')
n = 10
print(f"The first {n} natural numbers are: ", end='')   
print_natural_numbers(n)

#Create a function to calculate sum of first N natural numbers.
def sum_natural_numbers(n):
    return n * (n + 1) // 2
n = 10
print(f"The sum of the first {n} natural numbers is: {sum_natural_numbers(n)}")

#Create a function to reverse a number.
def reversed_number(num):
    rev_num = 0
    while num > 0:
        digit = num % 10
        rev_num = (rev_num * 10) + digit
        num //= 10
    return rev_num
num = 12345
print(f"The reverse of the number {num} is: {reversed_number(num)}")

#Create a function to count digits in a number.
def count_digits(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count
num = 12345
print(f"The number of digits in {num} is: {count_digits(num)}")

#Create a function to check palindrome number.
def is_palindrome(num):
    orig_num = num
    rev_num = 0
    while num > 0:
        digit = num % 10
        rev_num = (rev_num * 10) + digit
        num //= 10
    return orig_num == rev_num
num = 12321
if is_palindrome(num):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")

'''Calculator Using Functions that contains the following features:
    -	User selects operation 
	-	Program performs calculation 
	-	Display result'''
def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid input. Please select a valid operation.")
calculator()

#Create a text file and store student details.
student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")
class_name = input("Enter class/section: ")
with open("student_details.txt", "w") as file:
    file.write(f"Name: {student_name}\n")
    file.write(f"Roll Number: {roll_number}\n")
    file.write(f"Class/Section: {class_name}\n")
print("Student details have been saved to student_details.txt")

#Read data from a file. 
with open("student_details.txt", "r") as file:
    data = file.read()
    print("Student Details from file:")
    print(data)

#Handle division by zero using exception handling. 
def safe_division(num1, num2):
    try:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
safe_division(num1, num2)

#Create a Student class with name and marks.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
student_name = input("Enter student name: ")
student_marks = float(input("Enter student marks: "))
student = Student(student_name, student_marks)
student.display_info()



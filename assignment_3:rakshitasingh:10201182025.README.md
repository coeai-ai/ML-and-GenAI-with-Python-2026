#Q1. Create a function to print first 10 natural numbers
def natural_numbers():
    for i in range(1,11):
        print(i)

natural_numbers()


#Q2. Create a fucntion to calculate sum of first 10 natural number
def natural_sum():
    sum = 0 
    for i in range(1,11):
        sum = sum + i
        print(sum)

natural_sum()


#Q3. Create a function to reverse a number
def reverse_number():
    num = int(input("Enter a number: "))
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    print("Reverse =", rev)

reverse_number()


#Q4. Create a function to count digits in a number
def count_num():
    
    num = int(input("enter the number:"))
    count = print("the total digits are:",len(str(num)))

count_num()


#Q5. Create a function to check palindrome number
def palindrome():
    num = int(input("Enter a number: "))

    if str(num) == str(num)[::-1]:
        print("Palindrome")
    else:
        print("Not a Palindrome")

palindrome()

        
#Q6. Create a function to generate Fibonacci    
def fibonacci():
    n = int(input("Enter the number of terms: "))

    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci()


#Q7. Calculator Using Functions that contains the following features;
    #-  User selects operation Program performs calculation Display result
def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b 

def div(a,b):
    if b == 0:
        return "Division by zero is not possible"
    return a / b

print("Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result =", add(num1, num2))
elif choice == 2:
    print("Result =", sub(num1, num2))
elif choice == 3:
    print("Result =", mul(num1, num2))
elif choice == 4:
    print("Result =", div(num1, num2))
else:
    print("Invalid Choice")


#Q8. Create a text file and store student details.
file = open("student.txt", "w")

name = input("Enter student name: ")
roll = input("Enter roll number: ")
course = input("Enter course: ")

file.write("Name: " + name + "\n")
file.write("Roll Number: " + roll + "\n")
file.write("Course: " + course + "\n")

file.close()
print("Student details saved successfully.")


#Q9. Read data from file
file = open("student.txt", "r")

data = file.read()

print("Student Details:")
print(data)

file.close()

#Q10. Handle division by zero using exception handling
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))

    result = a / b

    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Please enter valid numbers.")
    

#Q11. Create a Student class with name and marks
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)


name = input("Enter student name: ")
marks = int(input("Enter marks: "))

s1 = Student(name, marks)

s1.display()
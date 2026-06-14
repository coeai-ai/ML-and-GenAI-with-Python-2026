#Aavani Prasad
#Assignment 3


#1 Function to print the first ten natural numbers
def print_natural_numbers(n):
    for i in range(1,n+1):
        print(i,end=' ')
print("First ten natural numbers:")
print_natural_numbers(10)

#2 Function to calculate sum of first N natural numbers
def sum_of_natural_numbers(n):
    s=sum(range(1,n+1))
    print(f"Sum of first {n} natural numbers = {s}")
sum_of_natural_numbers(5)

#3 Function to reverse a number
def to_reverse(n):
    return int(str(n)[::-1])
number=int(input("Enter number to reverse:"))
print(f"Reversed number is: {to_reverse(number)}")
         
#4 Function to count digits in a number
def count_digits(n):
    return len(str(n))
n=int(input("Enter a number to count its digits:"))
print(f"Number of digits in given number is {count_digits(n)}")

#5 Function to check palindrome number
def is_palindrome(n):
    if str(n)==str(n)[::-1]:
        print(f"{n} is a palindrome")
    else:
        print(f"{n} is not a palindrome")
is_palindrome(123)
is_palindrome(12321)

#6 Function to generate Fibonacci series
def fibonacci_series(n):
    a,b=0,1
    series=[]
    for i in range(n):
        series.append(a)
        a,b=b,a+b
    print("Required Fibonacci series:")
    print(series)
fibonacci_series(5)


#7 Calculator using functions
#Operations
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        print("Cannot be divided by zero!")
        return
    return a/b

#Choosing operations
def calculator():
    while True:
        print("CALCULATOR")
        print("1.Addition\n2.Subtraction\n3.Mutiplication\n4.Division\n5.Exit")
        
        choice=int(input("Enter operation number:"))
        if choice==1:
            a=float(input("Enter first number:"))
            b=float(input("Enter second number:"))
            print("Result=",add(a,b))
        elif choice==2:
            a=float(input("Enter first number:"))
            b=float(input("Enter second number:"))
            print("Result=",subtract(a,b))
        elif choice==3:
            a=float(input("Enter first number:"))
            b=float(input("Enter second number:"))
            print("Result=",multiply(a,b))
        elif choice==4:
            a=float(input("Enter first number:"))
            b=float(input("Enter second number:"))
            print("Result=",divide(a,b))
        elif choice==5:
            break
        else:
            print("Invalid input")
        print()
calculator()

#8 Create a text file and store student details 
def save_student_details(name,age,grade):
    with open("student_details.txt", "a") as file:
        file.write(f"Name: {name}, Age: {age}, Grade: {grade}\n")
student_name = input("Enter student name: ")
student_age = int(input("Enter student age: "))
student_grade = input("Enter student grade: ")
save_student_details(student_name, student_age, student_grade)
print("Student details saved to student_details.txt")  

#9 Read data from a file
def read_student_details():
    try:
        with open("student_details.txt", "r") as file:
            details = file.read()
            print("\n--- Student Details ---")
            print(details)
    except FileNotFoundError:
        print("No student details found. Please save some details first.")
read_student_details()

#10 Handle division by zero using exception handling
def handled_division(a,b):
    try:
        result=a/b
        return result
    except ZeroDivisionError:
        return" Cannot Divide by zero"
n1=float(input("Enter numerator:"))
n2=float(input("Enter denominator:"))
print("Final Result:", handled_division(n1,n2))

#11 Create Student class with name and marks
class Student:
    def _init_(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(f"Student Name:{self.name}")
        print("Marks:",self.marks)
        
name=input("Enter student name:")
marks=float(input("Enter marks:"))
s=Student(name,marks)
s.display

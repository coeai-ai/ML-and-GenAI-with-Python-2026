#Create a function to print first 10 natural numbers
def natural(n):
    for i in range(1,n+1):
        print(i)
natural(10)

#Create a function to calculate sum of first n natural numbers
def sum_nat(n):
    total=n*(n+1)//2
    print("Sum:\n",total)
sum_nat(10)

#Create a function to reverse a number 
def reverse(n):
    rev=0
    sum=0
    while n>0:
        rev=n%10
        sum=sum*10+rev
        n=n//10    
    print("Reverse of the number is:\n",sum)
num=int(input("Enter a number: "))
reverse(num)

#Create a function to count digits in a number
def count_digits(n):
    if n==0:
     return 1
    count=0
    while n>0:
        n=n//10
        count+=1
    print("Number of digits in the number is:\n",count)     
num=int(input("Enter a number: "))
count_digits(num)

#Create a functiom to check palindrome number
def palindrome(n):
    rev=0
    sum=0
    temp=n
    while n>0:
        rev=n%10
        sum=sum*10+rev
        n=n//10    
    if temp==sum:
        print("The number is a palindrome")
    else:
        print("The number is not a palindrome")
num=int(input("Enter a number: "))
palindrome(num)

#Create a function to generate fibonacci series
def fibo_series(n):
    a=0
    b=1
    for i in range(n):
        print(a,end=" ")
        c=a+b
        a=b
        b=c
n=int(input("Enter the number of terms:\n "))
fibo_series(n)

#Calculator using functions
def calculator():
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    operator=input("Enter the operator (+, -, *, /): ")
    if operator=="+":
        result=num1+num2
    elif operator=="-":
        result=num1-num2
    elif operator=="*":
        result=num1*num2
    elif operator=="/":
        result=num1/num2
    else:
        print("Invalid operator")
        return
    print("Result:",result)
calculator()

# Create a text file and store student details
def store_student_details():
    name=input("Enter the student's name: ")
    roll_num=int(input("Enter roll number: "))
    marks1=float(input("Enter marks for subject 1: "))
    marks2=float(input("Enter marks for subject 2: "))
    marks3=float(input("Enter marks for subject 3: "))
    with open("student_details.txt", "w") as file:
        file.write("Student Name: " + name + "\n")
        file.write("Roll Number: " + str(roll_num) + "\n")
        file.write("Marks for subject 1: " + str(marks1) + "\n")
        file.write("Marks for subject 2: " + str(marks2) + "\n")
        file.write("Marks for subject 3: " + str(marks3) + "\n")
store_student_details()

#Read data from the text file 
def read_student_details():
    with open("student_details.txt", "r") as file:
        details=file.read()
        print(details)
read_student_details()

#Handle division by zero error using exception handling
def division():
    try:
        num1=float(input("Enter the first number: "))
        num2=float(input("Enter the second number: "))
        result=num1/num2
        print("Result:",result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
division()

#Create student class with name and marks
class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    def display_details(self):
        print("Student Name:",self.name)
        print("Marks:",self.marks)
student1=Student("John", 85)
student1.display_details()


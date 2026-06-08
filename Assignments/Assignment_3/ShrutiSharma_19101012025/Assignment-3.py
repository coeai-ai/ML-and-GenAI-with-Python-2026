#ASSIGNMENT-3

#Create a function to print first 10 natural numbers
def natural_number():
    for i in range (1,11):
        print(i)
print("First 10 natural number are :\n")
natural_number()

#Create a function to calculate sum of first N natural numbers.
def sumn(n):
    s=0
    for i in range(1,n+1):
        s+=i
    print("sum of first n natural number is ",s)
t= int (input("Enter no of natural numbers:"))
sumn(t)

#Create a function to reverse a number.
def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev
n = int(input("Enter a number: "))
print("Reversed Number =", reverse_number(n))

#Create a function to count digits in a number.
def count_digit(num):
    c=0
    while num>0:
        c+=1
        num=num//10
    print("Total no of digits in this number is ",c)
num= int (input("Enter any number:"))
count_digit(num)

#Create a function to check palindrome number.
def palindrome_number(num):
    original = num
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    if original == rev:
        print("Palindrome Number!")
    else:
        print("Not a palindrome number!")
num = int(input("Enter any number: "))
palindrome_number(num)

#Create a function to generate Fibonacci series.
def fibonacci(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(n-2):
        c=a+b
        print(c)
        a=b
        b=c
n=int(input("Enter number of terms you want:"))
fibonacci(n)

#Calculator Using Functions that contains the following features: User selects operation, Program performs calculation, Display result
def add():
    sum= num1+ num2
    print(sum)
def subtract():
    sub= num1- num2
    print(sub)
def multiply():
    a= num1*num2
    print(a)
def division():
    div=num1/num2
    print(div)
def modulus():
    mod=num1%num2
    print(mod)
while True:
    num1= int(input("Enter First number:"))
    num2= int(input("Enter second number:"))
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus(remainder)")
    o= int(input("Enter which operation do you want to perform (1/2/3/4/5):"))
    if o==1:
        add()
    elif o==2:
        subtract()
    elif o==3:
        multiply()
    elif o==4:
        division()
    elif o==5:
        modulus()
    else:
        break
    ch= int(input("Do you to perform more operations(yes-1 or no-0):"))
    if ch==0:
        break

#Create a text file and store student details.
file=open("Student.txt","w")
file.write("Name: Shruti Sharma\n")
file.write("Enrollment Number: 19101012025\n")
file.write("College: IGDTUW\n")
print("Student details saved successfully.")

#Read data from a file.
with open("Student.txt", "r") as file:
    data = file.read()
print(data)

#Handle division by zero using exception handling.
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result =", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")

#Create a Student class with name and marks.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
s1 = Student("Shruti", 95)
s1.display()
    
    

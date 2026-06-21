#QUESTION 1
def natural_no():
    print("--- first 10 natural numbers ---")
    for i in range(1,11):
        print(i)
natural_no()

# QUESTION 2
def sum_natural_no(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

#QUESTION 3
def reverse():
    n = int(input("Enter no:> "))
    a = str(n)
    rev = int(a[ : :-1])
    return rev
     
print(reverse())

#QUESTION 4
def count_digits(n):
    a = len(str(n))
    return a

#QUESTION 5
def check_palindrome(n):
    a = int(str(n)[: :-1])
    if a == n:
        print(f"{n} is palindrome")
        return 
    else :
        print(f"{n} is not a palindrome")
        return
    
print(check_palindrome(151))
print(check_palindrome(15901))
print(check_palindrome(1221))

# QUESTION 6
def fibonacci_series():
    a = 0
    b = 1
    n = int(input("Enter the number of fibonacci series :>"))
    print (a,b, end = " ")
    for i in range(n):
        res = a  + b
        a = b
        b = res
        print(res , end = " ")

#   QUESTION 7
# Functions for calculations

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b

print("Select Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    result = add(num1, num2)
elif choice == 2:
    result = subtract(num1, num2)
elif choice == 3:
    result = multiply(num1, num2)
elif choice == 4:
    result = divide(num1, num2)
else:
    result = "Invalid Choice"


print("Result =", result)

# QUESTION 8

name = input("Enter name:> ")
roll_no = input("Enter roll no:> ")
marks = int(input("Enter marks: "))

with open("Students.txt", "a") as file:
    file.write(f"name : {name}\n")
    file.write(f"Roll no :{roll_no}\n")
    file.write(f"Marks: {marks}\n")
    
print("Student details saved successfully! ")

# QUESTION 9
with open("students.txt", "r") as file:
    data = file.read()

print(data)

# Question 10
try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    result = num1/num2
    print("Result = ",result)

except ZeroDivisionError:
    print("Error : Division by zero is not allowed.") 

# Question 11
class student:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def display(self):
        print("Name = ",self.name )
        print("Roll no = ",self.roll_no)
        print("Marks = ",self.marks )




#Create a function to print first 10 natural numbers.
def print_natural_numbers():
    for i in range(1,11):
        print(i)
print_natural_numbers()


#Create a function to calculate sum of first N natural numbers.
def sum(n):
    summ=0
    for i in range(1,n+1):
        summ+=i
    print(summ)
sum(9)

#Create a function to reverse a number.

def reverse_number(num):
    lastdigit=0
    rm=0
    while(num>0):
        lastdigit=num%10
        rm=rm*10+lastdigit
        num=num//10
    print(rm)

reverse_number(56)

def count_digits(num):
    count = 0

    while num > 0:
        count += 1
        num = num // 10
    print(count)
    

count_digits(7853)


#Create a function to check palindrome number

def is_palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        print("True")
    else:
        print ("False")


num = int(input("Enter a number: "))

is_palindrome(num)

#Create a function to generate Fibonacci series


def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        print(a,end="")
        c=a+b
        a=b
        b=c

n=int(input("Enter the number"))
fibonacci(n)

#  Calculator Using Functions
# Features:
# 1. User selects operation
# 2. Program performs calculation
# 3. Display result

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


print("Calculator Using Functions")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Select operation (1-4): "))

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


# Create a text file and store student details

file = open("student.txt", "w")

name = input("Enter name: ")
marks = input("Enter marks: ")

file.write("Name: " + name + "\n")
file.write("Marks: " + marks)

file.close()

print("Student details saved successfully.")


# Read data from a file

file = open("student.txt", "r")

data = file.read()
print(data)

file.close()

# Division by zero exception handling

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result =", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")



# Student class

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


name = input("Enter student name: ")
marks = int(input("Enter marks: "))

s1 = Student(name, marks)
s1.display()





    






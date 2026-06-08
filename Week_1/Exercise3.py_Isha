# 1. Function to print first 10 natural numbers
def num(n):
    for i in range(1,n+1):
        print(i,end=" ")
num(10)

# 2. Function to calculate sum of first N natural numbers
def get_sum(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
num=int(input("enter a num"))
print(get_sum(num))

# 3. Function to reverse a number
def rev(num):
    x=0
    while num>0:
        x=(x*10)+(num%10)
        num=num//10
    print(x)
n=int(input("enter a number"))
print(rev(n))

# 4. Function to count digits in a number
def count(num):
    x=0
    while num>0:
        x+=1
        num=num//10
    print(x)
n=int(input("enter a number"))
print(count(n))

# 5. Function to check palindrome number
def palindrome(num):
    temp = num
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    if temp == rev:
        print("Palindrome Number")
    else:
        print("Not a Palindrome Number")
num = int(input("Enter a number: "))
palindrome(num)

# 6. Function to generate Fibonacci series
def fibonacci(n):
    a = 0
    b = 1
    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
n = int(input("\nEnter number of terms: "))
fibonacci(n)

# 7. Calculator using functions

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b
choice = (input("Enter your choice: "))
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
if choice == "add":
    print("Result =", add(x, y))
elif choice == "sub":
    print("Result =", sub(x, y))
elif choice == "mul":
    print("Result =", mul(x, y))
elif choice == "div":
    print("Result =", div(x, y))
else:
    print("Invalid Choice")

# 8. Create a text file and store student details
file = open("student.txt", "w")
name = input("Enter student name: ")
roll = input("Enter roll number: ")
marks = input("Enter marks: ")
file.write("Name : " + name + "\n")
file.write("Roll No : " + roll + "\n")
file.write("Marks : " + marks)
file.close()
print("Student details saved.")

# 9. Read data from a file
file = open("student.txt", "r")
data = file.read()
print(data)
file.close()

# 10. Handle division by zero using exception handling
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result =", a / b)
except ZeroDivisionError:
    print("Division by zero is not possible.")

# 11. Create a Student class with name and marks
class Student:
    def getdata(self):
        self.name = input("Enter student name: ")
        self.marks = float(input("Enter marks: "))
    def display(self):
        print("Name :", self.name)
        print("Marks :", self.marks)
s1 = Student()
s1.getdata()
s1.display()




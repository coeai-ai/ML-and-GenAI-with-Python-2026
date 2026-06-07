# question 1
def counting(n):
    print("Counting till 10 first natural number")
    for i in range(1,n+1):
     print (i)

print(counting(10))

# question 2
def summation(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i

    return sum
print("Summation till nth  natural number is ",summation(10))

# question 3
def reverser(n):
    ans = 0
    while(n!=0):
      digit = n % 10
      ans = ans*10 + digit
      n = n // 10
    return ans
print("After reversing the number becomes ",reverser(104))

# question 4
def counting_digits(n):
    count = 0
    while(n!=0):
        count = count + 1
        n = n // 10
    return count
print ("The total digits of the number is ",counting_digits(879875))

# question 5
def reverser(n):
    ans = 0
    while(n!=0):
      digit = n % 10
      ans = ans*10 + digit
      n = n // 10
    return ans
def checking_palindrome(n):
    if (n==reverser(n)):
        print ("Palindrome")
    else:
        print ("Not Palindrome")
print(checking_palindrome(878))


# question 6
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


fibonacci(10)

# question 7
# Calculator using functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice (1-4): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result:", add(num1, num2))
elif choice == 2:
    print("Result:", subtract(num1, num2))
elif choice == 3:
    print("Result:", multiply(num1, num2))
elif choice == 4:
    print("Result:", divide(num1, num2))
else:
    print("Invalid choice")

# question 8
#  File Write
def add_student():
    name = input("Name: ")
    marks = input("Marks: ")

    with open("students.txt", "a") as f:
        f.write(name + "," + marks + "\n")

# question 9
#  File Read
def view_students():
    try:
        with open("students.txt", "r") as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("No file found")

# question 10
def divide(a, b):
    try:
        result = a / b
        print("Result:", result)

    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

divide(num1, num2)

# question 11
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

name = input("Enter student name: ")
marks = float(input("Enter marks: "))

s1 = Student(name, marks)
s1.display()
# 1. Print first 10 natural numbers
def print_natural():
    for i in range(1, 11):
        print(i)

print_natural()

# 2. Sum of first N natural numbers
def sum_natural(n):
    return n * (n + 1) // 2

n = int(input("Enter N: "))
print("Sum =", sum_natural(n))

# 3. Reverse a number
def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

num = int(input("Enter number: "))
print("Reverse =", reverse_number(num))

# 4. Count digits in a number
def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count

num = int(input("Enter number: "))
print("Digits =", count_digits(num))

# 5. Check palindrome number
def palindrome(num):
    temp = num
    rev = 0

    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10

    if num == rev:
        return True
    return False

num = int(input("Enter number: "))

if palindrome(num):
    print("Palindrome")
else:
    print("Not Palindrome")

# 6. Fibonacci series
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter number of terms: "))
fibonacci(n)

# 7. Calculator using functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice: "))
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print("Result =", add(a, b))
elif choice == 2:
    print("Result =", subtract(a, b))
elif choice == 3:
    print("Result =", multiply(a, b))
elif choice == 4:
    print("Result =", divide(a, b))
else:
    print("Invalid Choice")


#8 Create a text file and store student details
with open("studentmarks.txt", "w") as file:
file.write("Ishika:90\n Alice:85")


#9.Read data from a file
with open("studentmarks.txt","r") as file:
content file.read()
print(content)


#10 Handle division by zero
def divide(a, b):
    try:
        print("Result =", a / b)
    except ZeroDivisionError:
        print("Division by zero is not allowed")

a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))
divide(a, b)


# 11. Student class with name and marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Ishika", 90)
s1.display()
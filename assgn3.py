def print_first_10():
    for i in range(1, 11):
        print(i)

print_first_10()

def sum_n(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

n = 5
print("Sum:", sum_n(n))

def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

print("Reverse:", reverse_number(1234))

def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count

print("Digits:", count_digits(98765))

def is_palindrome(num):
    original = num
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return original == rev

num = 121
if is_palindrome(num):
    print("Palindrome")
else:
    print("Not Palindrome")

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    return "Cannot divide by zero"

print("Add:", add(10, 5))
print("Subtract:", subtract(10, 5))
print("Multiply:", multiply(10, 5))
print("Divide:", divide(10, 5))

def write_student_file():
    file = open("students.txt", "w")
    file.write("Name: Rahul, Marks: 85\n")
    file.write("Name: Priya, Marks: 92\n")
    file.write("Name: Amit, Marks: 78\n")
    file.close()

write_student_file()
print("File created successfully")

def read_student_file():
    file = open("students.txt", "r")
    data = file.read()
    file.close()
    print(data)

read_student_file()

def divide(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

divide(10, 2)
divide(10, 0)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Rahul", 88)
s2 = Student("Priya", 95)

s1.display()
print("----")
s2.display()


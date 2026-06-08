#1. Function to print first 10 natural numbers
def natural_numbers():
    for i in range(1, 11):
        print(i)

natural_numbers()

#2. Function to calculate sum of first N natural numbers
def sumnatural_nos(n):
    return n * (n + 1) // 2
sumnatural_nos(50)

# 3.Function to reverse a number
def reverse_number(m):
    return int(str(m)[::-1])  #firstly changing the num into string and applying string methods
reverse_number(133452)

# 4.Function to count digits in a number
def count_digits(num):
    return len(str(num))
count_digits(4532)

#5. Function to check palindrome number
def is_palindrome(p):
    return str(p) == str(p)[::-1]
is_palindrome(5225)

#6. Function to generate Fibonacci series up to N terms
def fibonacci(n):
    l = []
    a, b = 0, 1
    for i in range(n):
        l.append(a)
        a, b = b, a + b
    return l
fibonacci(7)


# 7. Calculator using functions
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"Result: {n1 + n2}")
    elif choice == '2':
        print(f"Result: {n1 - n2}")
    elif choice == '3':
        print(f"Result: {n1 * n2}")
    elif choice == '4':
        if n1 != 0:
            print(f"Result: {n1 / n2}")
        else:
            print("Error: Division by zero")
    else:
        print("Invalid choice")

# 8. Create a text file and store student details
with open("students.txt", "w") as f:
    f.write("Name: Payal, Marks: 85\n")
    f.write("Name: Rahul, Marks: 90\n")
    f.write("Name: Sneha, Marks: 78\n")
    
# 9. Read data from a file
try:
    with open("students.txt", "r") as f:
        data = f.read()
    print(data)
except FileNotFoundError:
    print("File not found.")

# 3. Handle division by zero using exception handling
a=int(input("enter numerator"))
b=int(input("enter  denominator"))
try:
    result = a / b
    print(f"\nDivision result: {result}")
except ZeroDivisionError:
    print("\nError: Division by zero is not allowed.")

# 4. Create a Student class with name and marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}, Marks: {self.marks}")


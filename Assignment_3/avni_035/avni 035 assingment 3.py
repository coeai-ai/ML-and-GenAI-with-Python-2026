#print the first 10 natural numbers
def print_natural_numbers(n):
    for i in range(1, n + 1):
        print(i)
print_natural_numbers(10)

#calculate the sum of the first n natural numbers
def sum_natural_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_natural_numbers(5))

#create a function to reverse a number
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num
print(reverse_number(12345))

#count digits in a number
def count_digits(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count
print(count_digits(12345))

#check is naymber is palindrome or not
def is_palindrome(num):
    return num == reverse_number(num)
print(is_palindrome(12321))
print(is_palindrome(12345))

#generate Fibonacci series up to n terms
def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
fibonacci_series(10)

#calculator using functions
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error! Division by zero."

def calculator():
    print("\n--- Calculator Menu ---")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    
    choice = input("Select operation (1-5): ")
    
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")
    elif choice == '5':
        print("Exiting calculator.")
    else:
        print("Invalid Selection!")

#file handling create ,write,and read student details
def file_handling():
    filename = "students.txt"
    
    # Create and write to the file
    with open(filename, 'w') as file:
        file.write("Name, Age, Grade\n")
        file.write("Alice, 20, A\n")
        file.write("Bob, 22, B\n")
        file.write("Charlie, 21, A-\n")
    # Read the file
    with open(filename, 'r') as file:
        content = file.read()
        print("\n--- Student Details ---")
        print(content)  
file_handling() 

    # handle division by zero using exception handling
def safe_divide(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Error! Division by zero."
print(safe_divide(10, 2))
print(safe_divide(10, 0))

#create a student class with name and marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")
student1 = Student("Alice", 85)
student1.display()

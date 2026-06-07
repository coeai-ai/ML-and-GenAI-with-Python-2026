def print_first_10_natural_numbers():
    print("First 10 natural numbers:")
    for i in range(1, 11):
        print(i, end=" ")
    print()



def sum_of_n_natural_numbers(n):
    if n < 1:
        return 0
    return sum(range(1, n + 1))



def reverse_number(num):
    # Convert to string, reverse it, and handle potential negative numbers
    sign = -1 if num < 0 else 1
    reversed_num = int(str(abs(num))[::-1])
    return sign * reversed_num



def count_digits(num):
    return len(str(abs(num)))



def is_palindrome(num):
    # A number is a palindrome if it reads the same backward as forward
    return str(num) == str(num)[::-1]

# Example call:
test_num = 121
print(f"Is {test_num} a palindrome? {is_palindrome(test_num)}")

def generate_fibonacci(terms):
    if terms <= 0:
        return []
    elif terms == 1:
        return [0]
    
    series = [0, 1]
    while len(series) < terms:
        series.append(series[-1] + series[-2])
    return series



def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error! Division by zero."

def calculator():
    print("\n--- Simple Calculator ---")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    choice = input("Select operation (1/2/3/4): ")
    
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1': print(f"Result: {add(num1, num2)}")
        elif choice == '2': print(f"Result: {subtract(num1, num2)}")
        elif choice == '3': print(f"Result: {multiply(num1, num2)}")
        elif choice == '4': print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid choice!")



def write_student_details(filename="students.txt"):
    with open(filename, "w") as file:
        file.write("Name: John Doe, Roll No: 101, Grade: A\n")
        file.write("Name: Jane Smith, Roll No: 102, Grade: B\n")
    print(f"Details written to {filename} successfully.")

def read_student_details(filename="students.txt"):
    print(f"\nReading data from {filename}:")
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found! Please write data to the file first.")

# Executing file operations:
write_student_details()
read_student_details()

def safe_division():
    try:
        numerator = float(input("\nEnter numerator: "))
        denominator = float(input("Enter denominator: "))
        result = numerator / denominator
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: You cannot divide a number by zero!")
    except ValueError:
        print("Error: Please enter valid numerical values.")



class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # Expects a list of marks or a single value

    def display_details(self):
        print(f"\n--- Student Object Details ---")
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")


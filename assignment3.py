#1 Create a function to print first 10 natural numbers
def print_first_10_natural_numbers():
    for i in range(1, 11):
        print(i, end=" ")
    print() 


#2 Function to calculate sum of first N natural numbers
def sum_of_n_natural_numbers(n):
    return (n * (n + 1)) // 2
# Example 
n = 5
print(f"Sum of first {n} natural numbers:", sum_of_n_natural_numbers(n))


#3 Function to reverse a number.
def reverse_number(num):
    reverse = 0
    while num > 0:
        remainder = num % 10
        reverse = (reverse * 10) + remainder
        num = num // 10
    return reverse
# Example 
number = 12345
print(f"Reverse of {number}:", reverse_number(number))


#4 Count digits in a number.
def count_digits(num):
    if num == 0:
        return 1 
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count
# Example 
num_to_count = 987654
print(f"Number of digits in {num_to_count}:", count_digits(num_to_count))


#5 Check palindrome number
def is_palindrome(num):
    # A palindrome number is equal to its reverse
    return num == reverse_number(num)
# Example
test_num = 121
print(f"Is {test_num} a palindrome?", is_palindrome(test_num))


#6 Fibonacci series upto N terms
def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series
# Example 
terms = 8
print(f"Fibonacci series ({terms} terms):", generate_fibonacci(terms))


#7 Calculator using functions
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b

def calculator():
    print("\n--- Simple Calculator ---")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
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
            # Basic check, though handled explicitly below via Exception Handling
            if num2 == 0:
                print("Error: Cannot divide by zero!")
            else:
                print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid Input")

# Example usage:
calculator()

#8 Create text files and store details
def store_student_details(filename, student_data):
    with open(filename, 'w') as file:
        for student in student_data:
            file.write(f"Name: {student['name']}, Marks: {student['marks']}\n")
    print(f"Data successfully written to {filename}")

def read_student_details(filename):
    print(f"\nReading data from {filename}:")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found! Please write to the file first.")
# Example
file_name = "students.txt"
students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 92}
]

store_student_details(file_name, students)

#9 Read the file
read_student_details(file_name)



#10 Handle division by zero using exception handling
def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
# Example
print("Valid Division (10 / 2):", safe_divide(10, 2))
print("Invalid Division (10 / 0):", safe_divide(10, 0))



#11 Create a Student class with name and marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_details(self):
        print(f"Student Name: {self.name}, Marks: {self.marks}")
# Example
student1 = Student("Charlie", 78)
student1.display_details()

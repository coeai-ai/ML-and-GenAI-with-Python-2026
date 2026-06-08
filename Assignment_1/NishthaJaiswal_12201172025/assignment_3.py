#Question 1:Function to print first 10 natural numbers
def print_ten_numbers():
    print("1. First 10 natural numbers:")
    for i in range(1, 11):
        print(i, end=" ")
    print()

print_ten_numbers()

#Question 2:Function to calculate sum of first N natural numbers
def sum_n_numbers(n):
    total = sum(range(1, n + 1))
    print(f"2. Sum of first {n} natural numbers is:", total)

sum_n_numbers(10)  # Using 10 as an example

#Question 3:Function to reverse a number
def reverse_number(num):
    reversed_num = int(str(num)[::-1])
    print(f"3. Reversal of {num} is:", reversed_num)

reverse_number(1234)  # Using 1234 as an example

#Question 4:Function to count digits in a number
def count_digits(num):
    digits = len(str(abs(num)))
    print(f"4. Number of digits in {num} is:", digits)

count_digits(98765)  # Using 98765 as an example

#Question 5:Function to check palindrome number
def check_palindrome(num):
    is_palindrome = str(num) == str(num)[::-1]
    print(f"5. Is {num} a palindrome?:", is_palindrome)

check_palindrome(121)  # Using 121 as an example

#Question 6:Function to generate Fibonacci series
def generate_fibonacci(n):
    print(f"6. Fibonacci series up to {n} terms:")
    n1, n2 = 0, 1
    for _ in range(n):
        print(n1, end=" ")
        n1, n2 = n2, n1 + n2
    print()

generate_fibonacci(10)

#Question 7:Calculator Using Functions
def calculator():
    print("\n--- 🧮 SIMPLE CALCULATOR ---")
    print("Choose operation: 1. Add  2. Subtract  3. Multiply  4. Divide")
    choice = input("Enter choice (1/2/3/4): ")
    
    # 9. Handle division by zero using exception handling
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print("Result:", num1 + num2)
        elif choice == '2':
            print("Result:", num1 - num2)
        elif choice == '3':
            print("Result:", num1 * num2)
        elif choice == '4':
            print("Result:", num1 / num2)
        else:
            print("Invalid Choice")
    except ZeroDivisionError:
        print("Error: You tried to divide by zero! That's a computer no-no!")
    except ValueError:
        print("Error: Please only type real numbers!")

calculator()

#Question 8:Create a text file, store student details, and read data from it
print("\n---  FILE HANDLING ---")
# Writing to a file
with open("student_details.txt", "w") as file:
    file.write("Student Name: Nishtha Jaiswal\n")
    file.write("Enrollment Number: 12201172025\n")
print("Saved student details into 'student_details.txt'!")

# Reading from a file
print("Reading data back from the file:")
with open("student_details.txt", "r") as file:
    print(file.read())

#Question 10:Create a Student class with name and marks
print("---  CLASS AND OBJECT ---")
class Student:
    def _init_(self, name, marks):
        self.name = name
        self.marks = marks
        
    def display(self):
        print(f"Student Class Object -> Name: {self.name}, Marks: {self.marks}")

# Making a student object
s = Student("Nishtha", 98)
s.display()
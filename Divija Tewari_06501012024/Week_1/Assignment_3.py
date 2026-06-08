# ==========================================
# Assignment 3
# Name: Divija Tewari
# ==========================================

# Function to print first 10 natural numbers
def print_natural_numbers():
    print("First 10 Natural Numbers:")
    for i in range(1, 11):
        print(i, end=" ")
    print("\n")


# Function to calculate sum of first N natural numbers
def sum_n_natural_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


# Function to reverse a number
def reverse_number(num):
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return reverse


# Function to count digits in a number
def count_digits(num):
    count = 0

    while num > 0:
        count += 1
        num = num // 10

    return count


# Function to check palindrome number
def palindrome_number(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return original == reverse


# Function to generate Fibonacci series
def fibonacci_series(n):
    a = 0
    b = 1

    print("Fibonacci Series:")

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

    print("\n")


# Calculator Functions
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Division by zero is not possible."
    return a / b


# Calculator Program
def calculator():
    print("\nCalculator Using Functions")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice (1-4): "))

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result =", add(num1, num2))

    elif choice == 2:
        print("Result =", subtract(num1, num2))

    elif choice == 3:
        print("Result =", multiply(num1, num2))

    elif choice == 4:
        print("Result =", divide(num1, num2))

    else:
        print("Invalid Choice")


# ==========================
# Main Program
# ==========================

print_natural_numbers()

n = int(input("Enter N for sum of first N natural numbers: "))
print("Sum =", sum_n_natural_numbers(n))

number = int(input("\nEnter a number to reverse: "))
print("Reversed Number =", reverse_number(number))

number = int(input("\nEnter a number to count digits: "))
print("Number of Digits =", count_digits(number))

number = int(input("\nEnter a number to check palindrome: "))
if palindrome_number(number):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

terms = int(input("\nEnter number of Fibonacci terms: "))
fibonacci_series(terms)

calculator()

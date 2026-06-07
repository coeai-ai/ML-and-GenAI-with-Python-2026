# 1. Function to print first 10 natural numbers

def print_natural_numbers():
    print("First 10 Natural Numbers:")
    
    for i in range(1, 11):
        print(i, end=" ")
    
    print()


# 2. Function to calculate sum of first N natural numbers

def sum_natural_numbers(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total


# 3. Function to reverse a number

def reverse_number(num):
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return reverse


# 4. Function to count digits in a number

def count_digits(num):
    count = 0

    while num > 0:
        num = num // 10
        count += 1

    return count


# 5. Function to check palindrome number

def palindrome_number(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        return True
    else:
        return False


# 6. Function to generate Fibonacci series

def fibonacci_series(n):
    a = 0
    b = 1

    print("Fibonacci Series:")

    for i in range(n):
        print(a, end=" ")

        c = a + b
        a = b
        b = c

    print()


# 7. Calculator Using Functions

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b


def calculator():
    print("\nCalculator")
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



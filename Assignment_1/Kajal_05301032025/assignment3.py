# 1. Function to print first 10 natural numbers
def print_natural_numbers():
    print("First 10 Natural Numbers:")
    for i in range(1, 11):
        print(i, end=" ")
    print()


# 2. Function to calculate sum of first N natural numbers
def sum_natural_numbers(n):
    return n * (n + 1) // 2


# 3. Function to reverse a number
def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev


# 4. Function to count digits in a number
def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count


# 5. Function to check palindrome number
def is_palindrome(num):
    return num == reverse_number(num)


# 6. Function to generate Fibonacci series
def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci Series:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


# 7. Calculator using functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero not allowed"
    return a / b

def calculator():
    print("\nCalculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

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
        print("Invalid choice")


# -------- Main Program --------

print_natural_numbers()

n = int(input("Enter N for sum of natural numbers: "))
print("Sum =", sum_natural_numbers(n))

num = int(input("\nEnter a number to reverse: "))
print("Reversed Number =", reverse_number(num))

num = int(input("\nEnter a number to count digits: "))
print("Number of Digits =", count_digits(num))

num = int(input("\nEnter a number to check palindrome: "))
if is_palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

terms = int(input("\nEnter number of Fibonacci terms: "))
fibonacci(terms)

calculator()
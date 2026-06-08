# Assignment 3
# 1. Function to print first 10 natural numbers
def print_numbers():
    for i in range(1, 11):
        print(i, end=" ")
    print()


# 2.Function to find sum of first N natural numbers
def find_sum(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total


# 3. Function to reverse a number
def reverse_number(num):
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10

    return rev


# 4. Function to count digits
def count_digits(num):
    count = 0

    while num > 0:
        count += 1
        num //= 10

    return count


# 5. Function to check palindrome
def is_palindrome(num):
    original = num
    rev = reverse_number(num)

    if original == rev:
        return True
    else:
        return False


# 6. Function to print Fibonacci series
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

    print()


# 7. Calculator functions
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# Main Programs

print("First 10 Natural Numbers:")
print_numbers()

n = int(input("\nEnter N for sum: "))
print("Sum =", find_sum(n))

num = int(input("\nEnter a number to reverse: "))
print("Reversed Number =", reverse_number(num))

num = int(input("\nEnter a number to count digits: "))
print("Total Digits =", count_digits(num))

num = int(input("\nEnter a number to check palindrome: "))
if is_palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

terms = int(input("\nEnter number of Fibonacci terms: "))
print("Fibonacci Series:")
fibonacci(terms)

print("\nCalculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice: "))

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
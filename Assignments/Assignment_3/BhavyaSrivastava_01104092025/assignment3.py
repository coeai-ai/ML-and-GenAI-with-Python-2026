# 1. Print first 10 natural numbers
def print_first_10_natural_numbers():
    print("First 10 Natural Numbers:")
    for i in range(1, 11):
        print(i, end=" ")
    print("\n")


# 2. Sum of first N natural numbers
def sum_natural_numbers(n):
    return n * (n + 1) // 2


# 3. Reverse a number
def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev


# 4. Count digits in a number
def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count


# 5. Check palindrome number
def is_palindrome(num):
    return num == reverse_number(num)


# 6. Generate Fibonacci series
def fibonacci(n):
    a, b = 0, 1
    series = []

    for _ in range(n):
        series.append(a)
        a, b = b, a + b

    return series


# 7. Calculator Using Functions
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b


def calculator():
    print("\nCalculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1-4): ")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(a, b))
    elif choice == '2':
        print("Result:", subtract(a, b))
    elif choice == '3':
        print("Result:", multiply(a, b))
    elif choice == '4':
        print("Result:", divide(a, b))
    else:
        print("Invalid choice")

print_first_10_natural_numbers()

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

n = int(input("\nEnter number of Fibonacci terms: "))
print("Fibonacci Series:", fibonacci(n))

calculator()
# 1. Print first 10 natural numbers

def print_first_10():
    for i in range(1, 11):
        print(i, end=" ")
    print()

print_first_10()

# 2. Sum of first N natural numbers

def sum_of_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Enter N: "))
print(f"Sum of first {n} natural numbers = {sum_of_n(n)}")

# 3. Reverse a number

def reverse_number(num):
    reversed_num = 0
    original = num
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num

num = int(input("Enter a number: "))
print(f"Reversed number = {reverse_number(num)}")

# 4. Count digits in a number

def count_digits(num):
    count = 0
    num = abs(num)
    if num == 0:
        return 1
    while num != 0:
        num //= 10
        count += 1
    return count

num = int(input("Enter a number: "))
print(f"Number of digits = {count_digits(num)}")

# 5. Check palindrome number

def is_palindrome(num):
    original = num
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return original == reversed_num

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")

# 6. Generate Fibonacci series

def fibonacci(n):
    if n <= 0:
        print("Enter a positive number")
        return
    a, b = 0, 1
    print("Fibonacci series:", end=" ")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

n = int(input("How many terms? "))
fibonacci(n)

# 7. Calculator using functions

def add(a, b):      return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator():
    print("\n--- Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Select operation (1/2/3/4): ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if   choice == "1": result = add(a, b)
    elif choice == "2": result = subtract(a, b)
    elif choice == "3": result = multiply(a, b)
    elif choice == "4": result = divide(a, b)
    else: result = "Invalid choice"
    print(f"Result = {result}")

calculator()


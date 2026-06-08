# Program 1: Print First 10 Natural Numbers

def print_natural_numbers():
    print("First 10 Natural Numbers:")
    for i in range(1, 11):
        print(i, end=" ")
    print()

print_natural_numbers()


# Program 2: Sum of First N Natural Numbers

def sum_n_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("\nEnter value of N: "))
print("Sum =", sum_n_numbers(n))


# Program 3: Reverse a Number

def reverse_number(num):
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return reverse

num = int(input("\nEnter a number to reverse: "))
print("Reversed Number =", reverse_number(num))


# Program 4: Count Digits in a Number

def count_digits(num):
    count = 0

    while num > 0:
        count += 1
        num = num // 10

    return count

num = int(input("\nEnter a number: "))
print("Total Digits =", count_digits(num))


# Program 5: Check Palindrome Number

def palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        print("Palindrome Number")
    else:
        print("Not a Palindrome Number")

num = int(input("\nEnter number to check palindrome: "))
palindrome(num)


# Program 6: Fibonacci Series

def fibonacci(n):
    a = 0
    b = 1

    print("Fibonacci Series:")

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

    print()

terms = int(input("\nEnter number of terms: "))
fibonacci(terms)


# Program 7: Calculator Using Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero not possible"
    return a / b

print("\n===== Calculator =====")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Choose operation (1-4): "))

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
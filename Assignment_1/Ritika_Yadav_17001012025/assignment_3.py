# Function to print first 10 natural numbers

def print_natural_numbers():
    for i in range(1, 11):
        print(i, end=" ")

print_natural_numbers()


# Function to calculate sum of first N natural numbers

def sum_natural_numbers(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total

n = int(input("Enter a number: "))
print("Sum =", sum_natural_numbers(n))



# Function to reverse a number

def reverse_number(num):
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return reverse

num = int(input("Enter a number: "))
print("Reversed Number =", reverse_number(num))




# Function to count digits in a number

def count_digits(num):
    count = 0

    while num > 0:
        count += 1
        num = num // 10

    return count

num = int(input("Enter a number: "))
print("Number of digits =", count_digits(num))





# Function to check palindrome number

def is_palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return original == reverse

num = int(input("Enter a number: "))

if is_palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")



# Function to generate Fibonacci Series

def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        next_term = a + b
        a = b
        b = next_term

n = int(input("Enter number of terms: "))
fibonacci(n)
   


# Calculator Using Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not possible"
    return a / b

print("===== CALCULATOR =====")
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

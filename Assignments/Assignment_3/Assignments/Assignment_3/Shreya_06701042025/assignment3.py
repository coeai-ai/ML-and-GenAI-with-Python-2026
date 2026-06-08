
# Function to print first 10 natural numbers

def print_numbers():
    for i in range(1, 11):
        print(i)

print_numbers()


# Function to find sum of first N natural numbers

def sum_natural(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total

n = int(input("Enter N: "))
print("Sum =", sum_natural(n))



# Function to reverse a number

def reverse_number(num):
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return reverse

num = int(input("Enter a number: "))
print("Reverse =", reverse_number(num))



# Function to count digits

def count_digits(num):
    count = 0

    while num > 0:
        count += 1
        num = num // 10

    return count

num = int(input("Enter a number: "))
print("Number of digits =", count_digits(num))



# Function to check palindrome

def palindrome(num):
    if str(num) == str(num)[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

num = input("Enter a number: ")
palindrome(num)

# Function to generate Fibonacci series

def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

n = int(input("Enter number of terms: "))
fibonacci(n)


# Calculator using functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

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
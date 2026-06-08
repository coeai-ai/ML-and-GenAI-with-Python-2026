8595# 1. Function to print first 10 natural numbers
def print_natural_numbers():
    for i in range(1, 11):
        print(i, end=" ")
print_natural_numbers()


# 2. Function to calculate sum of first N natural numbers
def sum_natural_numbers(n):
    return n * (n + 1) // 2
print(sum_natural_numbers(10))

def reverse_number(num):
    return str(num)[::-1]

# 3. Write a Function to Reverse a Number
def reverse_number(num):
    return int(str(num)[::-1])

num = int(input("Enter a number: "))
print(reverse_number(num))

# 4. Write a Function to Count Digits in a Number

def count_digits(num):
    count = 0
    for digit in str(num):
        count += 1
    return count

num = int(input("Enter a number: "))
print("Number of Digits =", count_digits(num))

# 5. Write a Function to Check Whether a Number is Palindrome or Not

def is_palindrome(num):
    num = str(num)
    return num == num[::-1]
num = input("Enter a number: ")

if is_palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

# 6. Write a Function to Generate Fibonacci Series
def fibonacci(n):
    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter number of terms: "))
fibonacci(n)

# 7. Calculator Using Functions
def calculator():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice (1-4): "))

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Result =", a + b)

    elif choice == 2:
        print("Result =", a - b)

    elif choice == 3:
        print("Result =", a * b)

    elif choice == 4:
        if b != 0:
            print("Result =", a / b)
        else:
            print("Division by zero is not possible")

    else:
        print("Invalid Choice")

calculator()

# 8. Create a Text File and Store Student Details
name = input("Enter student name: ")
roll = input("Enter roll number: ")
marks = input("Enter marks: ")

file = open("student.txt", "w")

file.write("Name: " + name + "\n")
file.write("Roll Number: " + roll + "\n")
file.write("Marks: " + marks)

file.close()

print("Student details saved successfully.")

# 9. Read Data from a File
file = open("student.txt", "r")
data = file.read()

print("Student Details:")
print(data)

file.close()

# 10. Handle Division by Zero Using Exception Handling

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


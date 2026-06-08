# Sum of first 10 natural numbers
total = 0
for i in range (1, 11):
    total += i
print("Sum of first 10 natural numbers:", total)

# Factorial of a number
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("Factorial of 0 is 1.")
else:
    for k in range(1, num + 1):
        factorial *= k
    print("Factorial of", num, "is", factorial)

# Fibonacci Series
n_terms = int(input("Enter the number of terms for Fibonacci series: "))
n1, n2 = 0, 1
count = 0
if n_terms <= 0:
    print("Please enter a positive integer.")
elif n_terms == 1:
    print("Fibonacci sequence up to", n_terms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < n_terms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

# Find Largest Among Three Numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print("The largest number is", largest)

# Create Student Result System using if-elif-else, loops and user input
num_students = int(input("Enter the number of students: "))
for i in range(num_students):
    name = input("Enter the name of student {}: ".format(i + 1))
    marks = float(input("Enter the marks of {}: ".format(name)))
    if marks >= 90:
        grade = 'A'
    elif marks >= 80:
        grade = 'B'
    elif marks >= 70:
        grade = 'C'
    elif marks >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print("Student: {}, Marks: {}, Grade: {}".format(name, marks, grade))
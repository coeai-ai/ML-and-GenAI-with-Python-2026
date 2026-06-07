# ==========================================
# ASSIGNMENT 2
# ==========================================

print("--- 1. Find Sum of First 10 Natural Numbers ---")
# Using a for loop and range() to iterate from 1 to 10
sum_natural = 0
for i in range(1, 11):
    sum_natural += i  # Add current number to the sum

print(f"The sum of the first 10 natural numbers is: {sum_natural}")

# EXPECTED OUTPUT:
# --- 1. Find Sum of First 10 Natural Numbers ---
# The sum of the first 10 natural numbers is: 55
print("\n" + "="*40 + "\n")


print("--- 2. Find Factorial of a Number ---")
# Using sample data: number = 5
number = 5
factorial = 1

# Check if the number is negative, zero, or positive
if number < 0:
    print("Factorial does not exist for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1")
else:
    # Loop from 1 up to the given number to calculate factorial
    for i in range(1, number + 1):
        factorial *= i  # Multiply current number to factorial
    print(f"The factorial of {number} is: {factorial}")

# EXPECTED OUTPUT:
# --- 2. Find Factorial of a Number ---
# The factorial of 5 is: 120
print("\n" + "="*40 + "\n")


print("--- 3. Print Fibonacci Series ---")
# Using sample data to print the first 8 terms of the Fibonacci series
terms = 8
# The first two terms of a Fibonacci series are always 0 and 1
n1, n2 = 0, 1

print(f"Fibonacci series up to {terms} terms:")
for _ in range(terms):
    print(n1, end=" ")  # Print the current term on the same line
    # Update values: next term is the sum of previous two
    next_term = n1 + n2
    n1 = n2
    n2 = next_term

print() # Adds a new line after the series completes

# EXPECTED OUTPUT:
# --- 3. Print Fibonacci Series ---
# Fibonacci series up to 8 terms:
# 0 1 1 2 3 5 8 13 
print("\n" + "="*40 + "\n")


print("--- 4. Find Largest Among 3 Numbers ---")
# Using sample data
num1 = 45
num2 = 78
num3 = 22

# Using if-elif-else logic to compare the numbers
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print(f"The numbers are: {num1}, {num2}, {num3}")
print(f"The largest number is: {largest}")

# EXPECTED OUTPUT:
# --- 4. Find Largest Among 3 Numbers ---
# The numbers are: 45, 78, 22
# The largest number is: 78
print("\n" + "="*40 + "\n")


print("--- 5. Student Result System ---")
# This section uses input(), loops, and if-elif-else as required by the assignment

# 1. Input student details
student_name = input("Enter Student's Name: ")
student_roll = input("Enter Roll Number: ")

total_subjects = 3
total_marks = 0

# 2. Input marks using a loop
print(f"--- Enter marks for {total_subjects} subjects (out of 100) ---")
for i in range(1, total_subjects + 1):
    # Loop to collect marks repeatedly
    mark = float(input(f"Enter marks for Subject {i}: "))
    total_marks += mark # Add the entered mark to the total

# 3. Calculate percentage
percentage = (total_marks / (total_subjects * 100)) * 100

# 4. Display grade using if-elif-else
grade = ""
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"

# Print final result
print("\n--- FINAL RESULT ---")
print(f"Student Name: {student_name}")
print(f"Roll Number:  {student_roll}")
print(f"Total Marks:  {total_marks} / {total_subjects * 100}")
print(f"Percentage:   {percentage:.2f}%")
print(f"Final Grade:  {grade}")

# EXPECTED OUTPUT (If you input: Rahul, 101, 85, 92, 78):
# --- 5. Student Result System ---
# Enter Student's Name: Rahul
# Enter Roll Number: 101
# --- Enter marks for 3 subjects (out of 100) ---
# Enter marks for Subject 1: 85
# Enter marks for Subject 2: 92
# Enter marks for Subject 3: 78
# 
# --- FINAL RESULT ---
# Student Name: Rahul
# Roll Number:  101
# Total Marks:  255.0 / 300
# Percentage:   85.00%
# Final Grade:  A

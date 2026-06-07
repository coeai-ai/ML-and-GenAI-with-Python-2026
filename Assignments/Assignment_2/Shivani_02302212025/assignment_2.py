# 1. Sum of first 10 natural numbers
print("=== Sum of First 10 Natural Numbers ===")
total = 0
for i in range(1, 11):
    total += i
print("Sum of first 10 natural numbers:", total)


# 2. Factorial of a number
print("\n=== Factorial of a Number ===")
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)


# 3. Fibonacci Series
print("\n=== Fibonacci Series ===")
terms = int(input("Enter number of terms: "))
a, b = 0, 1
for i in range(terms):
    print(a, end=" ")
    a, b = b, a + b
print()


# 4. Largest among 3 numbers
print("\n=== Largest Among 3 Numbers ===")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))
if x >= y and x >= z:
    print("Largest:", x)
elif y >= x and y >= z:
    print("Largest:", y)
else:
    print("Largest:", z)


# 5. Student Result System
print("\n=== Student Result System ===")
# Input student details
name = input("Enter student name: ")
roll = input("Enter roll number: ")
num_subjects = int(input("Enter number of subjects: "))

# Input marks using a loop
total_marks = 0
for i in range(1, num_subjects + 1):
    m = float(input("Enter marks in subject " + str(i) + ": "))
    total_marks += m

# Calculate percentage
percentage = total_marks / num_subjects

# Display grade using if-elif-else
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"

# Display result
print("\n--- Student Result ---")
print("Name:", name)
print("Roll Number:", roll)
print("Total Marks:", total_marks)
print("Percentage:", percentage, "%")
print("Grade:", grade)
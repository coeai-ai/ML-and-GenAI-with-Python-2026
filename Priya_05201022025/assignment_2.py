# Program 1: Sum of First 10 Natural Numbers

print("\nPROGRAM 1 : SUM OF FIRST 10 NATURAL NUMBERS")
total = 0
for i in range(1, 11):
    total += i

print("Sum =", total)


# Program 2: Factorial of a Number

print("\nPROGRAM 2 : FACTORIAL OF A NUMBER")
number = int(input("Enter a number: "))
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial =", factorial)


# Program 3: Fibonacci Series

print("\nPROGRAM 3 : FIBONACCI SERIES")
terms = int(input("Enter number of terms: "))
first = 0
second = 1

print("Fibonacci Series:")

for i in range(terms):
    print(first, end=" ")

    next_term = first + second
    first = second
    second = next_term

print()


# Program 4: Largest Among 3 Numbers

print("\nPROGRAM 4 : LARGEST AMONG 3 NUMBERS")
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("Largest Number =", largest)


# Program 5: Student Result System

print("\nPROGRAM 5 : STUDENT RESULT SYSTEM")
student_name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
total_marks = 0
for i in range(1, 6):
    marks = float(input(f"Enter marks of Subject {i}: "))
    total_marks += marks

percentage = total_marks / 5

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

print("\n========== STUDENT RESULT ==========")
print("Student Name:", student_name)
print("Roll Number:", roll_no)
print("Total Marks:", total_marks)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)

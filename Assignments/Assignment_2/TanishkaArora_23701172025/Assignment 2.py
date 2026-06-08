# Sum of first 10 natural numbers
total = 0

for i in range(1, 11):
    total = total + i

print("Sum of first 10 natural numbers:", total)

# Factorial of a number
num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial of", num, "is:", factorial)

# Fibonacci Series up to n terms
n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    next_term = a + b
    a = b
    b = next_term

# Find largest among 3 numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

# Student Result System
# Uses if-elif-else, loops, and user input

# ---------- Student Details ----------
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# ---------- Input Marks for 5 Subjects ----------
subjects = ["Maths", "Science", "English", "History", "Computer"]
marks = []

for subject in subjects:
    mark = float(input(f"Enter marks in {subject} (out of 100): "))
    marks.append(mark)

# ---------- Calculate Total and Percentage ----------
total = 0
for mark in marks:
    total = total + mark

percentage = (total / 500) * 100

# ---------- Determine Grade ----------
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
    grade = "F (Fail)"

# ---------- Display Result ----------
print("\n========== STUDENT RESULT ==========")
print("Name        :", name)
print("Roll No.    :", roll_no)
print("-------------------------------------")

for i in range(len(subjects)):
    print(f"{subjects[i]:<12}: {marks[i]}")

print("-------------------------------------")
print(f"Total       : {total} / 500")
print(f"Percentage  : {percentage:.2f}%")
print(f"Grade       : {grade}")
print("=====================================")
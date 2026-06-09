# 1. Find Sum of First 10 Natural Numbers
print("=" * 40)
print("1. Sum of First 10 Natural Numbers")
print("=" * 40)
total = 0
for i in range(1, 11):   # Loop from 1 to 10
    total += i
print(f"Sum of first 10 natural numbers = {total}")
 
 
# 2. Find Factorial of a Number
print("\n" + "=" * 40)
print("2. Factorial of a Number")
print("=" * 40)
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):   # Multiply from 1 to num
    factorial *= i
print(f"Factorial of {num} = {factorial}")
 
 
# 3. Print Fibonacci Series
print("\n" + "=" * 40)
print("3. Fibonacci Series")
print("=" * 40)
n = int(input("How many terms of Fibonacci series? "))
a, b = 0, 1
print("Fibonacci Series:", end=" ")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b   # Update next two terms
print()
 
 
# 4. Find Largest Among 3 Numbers
print("\n" + "=" * 40)
print("4. Largest Among 3 Numbers")
print("=" * 40)
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))
 
if x >= y and x >= z:
    print(f"Largest number = {x}")
elif y >= x and y >= z:
    print(f"Largest number = {y}")
else:
    print(f"Largest number = {z}")
 
 
# 5. Student Result System
print("\n" + "=" * 40)
print("5. Student Result System")
print("=" * 40)
 
# Input student details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
 
# Input marks for 5 subjects
subjects = ["English", "Math", "Science", "Hindi", "Computer"]
marks = []
 
for subject in subjects:
    mark = float(input(f"Enter marks in {subject} (out of 100): "))
    marks.append(mark)
 
# Calculate total and percentage
total = sum(marks)
percentage = (total / 500) * 100
 
# Determine grade using if-elif-else
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
    grade = "F (Fail)"
 
# Display result
print("\n======== Student Result ========")
print(f"Name       : {name}")
print(f"Roll No.   : {roll_no}")
print("--------------------------------")
for i in range(len(subjects)):
    print(f"{subjects[i]:<10} : {marks[i]}")
print("--------------------------------")
print(f"Total      : {total} / 500")
print(f"Percentage : {percentage:.2f}%")
print(f"Grade      : {grade}")
print("================================")

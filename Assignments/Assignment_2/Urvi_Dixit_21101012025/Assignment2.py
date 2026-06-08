# 1. Sum of first 10 natural numbers
sum_natural = 0
for i in range(1, 11):
    sum_natural += i
print("Sum of first 10 natural numbers =", sum_natural)


# 2. Factorial of a number
num = int(input("\nEnter a number to find factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "=", factorial)


# 3. Fibonacci Series
n = int(input("\nEnter number of terms for Fibonacci series: "))
a, b = 0, 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# 4. Find largest among 3 numbers
x = float(input("\n\nEnter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))

if x >= y and x >= z:
    largest = x
elif y >= x and y >= z:
    largest = y
else:
    largest = z

print("Largest number among", x, y, z, "is:", largest)


# 5. Student Result System
print("\n--- Student Result System ---")

# Input student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Input marks
subjects = ["Maths", "Science", "English"]
marks = []
for subject in subjects:
    mark = float(input(f"Enter marks in {subject}: "))
    marks.append(mark)

# Calculate percentage
total_marks = sum(marks)
percentage = (total_marks / (len(subjects) * 100)) * 100

# Display grade using if-elif-else
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "F"

# Display result
print("\n--- Student Report ---")
print("Name:", name)
print("Roll Number:", roll_no)
for i in range(len(subjects)):
    print(subjects[i], ":", marks[i])
print("Total Marks:", total_marks)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)

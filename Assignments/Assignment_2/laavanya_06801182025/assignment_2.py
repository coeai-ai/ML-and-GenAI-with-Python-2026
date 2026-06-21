#Find sum of first 10 natural numbers.

sum = 0
for i in range(1, 11):
    sum = sum + i
print("Sum of first 10 natural numbers =", sum)


#Find factorial of a number.

num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact = fact * i
print("Factorial =", fact)

#Print fibonacci series.

n = int(input("How many terms do you want? "))
a = 0
b = 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

#Find largest among 3 numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest number is", a)
elif b >= a and b >= c:
    print("Largest number is", b)
else:
    print("Largest number is", c)

#Create student result system.

print("===== STUDENT RESULT SYSTEM =====")
# Student Details
name = "Lavanya"
roll_no = "23CSE101"
branch = "CSE"
print("Student Name :", name)
print("Roll Number  :", roll_no)
print("Branch       :", branch)
# Marks
sub1 = 85   # Python
sub2 = 78   # Mathematics
sub3 = 92   # Data Structures
sub4 = 88   # English
sub5 = 81   # Computer Networks
print("\nMarks Obtained")
print("Python              :", sub1)
print("Mathematics         :", sub2)
print("Data Structures     :", sub3)
print("English             :", sub4)
print("Computer Networks   :", sub5)
# Calculate Total and Percentage
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5
# Grade Calculation
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
    grade = "F"
# Display Result
print("\n===== RESULT =====")
print("Total Marks :", total)
print("Percentage  :", percentage)
print("Grade       :", grade)
if grade == "F":
    print("Result      : FAIL")
else:
    print("Result      : PASS")
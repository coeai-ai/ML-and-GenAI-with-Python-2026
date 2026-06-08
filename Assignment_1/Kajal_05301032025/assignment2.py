# 1. Find Sum of First 10 Natural Numbers
sum = 0
for i in range(1, 11):
    sum += i
print("Sum =", sum)

# 2. Find Factorial of a Number
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial =", fact)

#3. Print Fibonacci Series
n = int(input("Enter number of terms: "))
a = 0
b = 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

# 4. Find Largest Among 3 Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number is:", largest)


# 5. Student Result System
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

subjects = 5
total_marks = 0

for i in range(1, subjects + 1):
    marks = float(input(f"Enter marks of Subject {i}: "))
    total_marks += marks

percentage = total_marks / subjects

print("\n----- RESULT -----")
print("Name:", name)
print("Roll No:", roll_no)
print("Total Marks:", total_marks)
print("Percentage:", percentage)

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

print("Grade:", grade)
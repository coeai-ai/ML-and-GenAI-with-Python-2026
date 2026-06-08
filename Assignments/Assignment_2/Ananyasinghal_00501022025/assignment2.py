#Find sum of first 10 natural numbers
sum = 0
for i in range(1, 11):
    sum = sum + i
print("Sum =", sum)

#Find factorial of a number.
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial =", factorial)

#Print Fibonacci Series.
n = int(input("Enter the number of terms: "))
a = 0
b = 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

#Create Student Result System
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
# Input marks
marks1 = float(input("Enter marks for Subject 1: "))
marks2 = float(input("Enter marks for Subject 2: "))
marks3 = float(input("Enter marks for Subject 3: "))

# Calculate total and percentage
total = marks1 + marks2 + marks3
percentage = total / 3

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
    grade = "F"
print("Name:", name)
print("Roll Number:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)


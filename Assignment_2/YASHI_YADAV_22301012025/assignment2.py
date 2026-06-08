#Assignment 2 by Yashi Yadav 22301012025

#***************************************************
# 1) Sum of first 10 natural numbers
sum = 0

for i in range(1, 11):
    sum += i

print("Sum of first 10 natural numbers =", sum)


#***************************************************
# 2)student result display

# Input Student Details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Input Marks
m1 = float(input("Enter marks in Subject 1: "))
m2 = float(input("Enter marks in Subject 2: "))
m3 = float(input("Enter marks in Subject 3: "))
m4 = float(input("Enter marks in Subject 4: "))
m5 = float(input("Enter marks in Subject 5: "))

# Calculate Total and Percentage
total = m1 + m2 + m3 + m4 + m5
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
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Display Result
print("\n----- STUDENT REPORT -----")
print("Name       :", name)
print("Roll No    :", roll_no)
print("Total Marks:", total)
print("Percentage :", percentage, "%")
print("Grade      :", grade)


#***************************************************
#3) display factorial

num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)

#***************************************************
#Fibonacci Series


n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

    
#***************************************************
#largest in 3 number

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number =", largest)
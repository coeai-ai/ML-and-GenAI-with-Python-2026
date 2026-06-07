
#Assignment 2

#1

sum = 0

for i in range(1,11):
    sum+=i

print("Sum of first 10 natural numbers: ", sum)


#2
def factorial(n):
    if(n==0) or (n==1):
        return 1
    else:
        return n*factorial(n-1)
    
n = int(input("Enter the number: "))
print("Factorial of given number n: ", factorial(n))

#3
# Number of terms
n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

#4
#Let the 3 numbers be a,b and c

# Taking input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Finding the largest number
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number is:", largest)

#5
# Student Result System

# Input student details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Input marks of 5 subjects using loop
total = 0

for i in range(1, 6):
    marks = float(input(f"Enter marks for Subject {i}: "))
    total += marks

# Calculate percentage
percentage = total / 5

# Determine grade
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

# Display result
print("\n----- STUDENT RESULT -----")
print("Name:", name)
print("Roll Number:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
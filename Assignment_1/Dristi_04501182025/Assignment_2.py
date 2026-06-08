#1 Sum of first ten natural numbers
sum=0
for i in range(11):
    sum+=i
print("The sum of the first ten natural numbers is:", sum)

#2 To calculate the fctorial of a number
n = int(input("Enter a number to calculate its factorial:"))
fact=1
for i in range(1, n+1):
    fact*=i
print("The factorial of the number is:", fact)

#3 To Print the fibonacci sequence up to n terms
n = int(input("Enter the number of terms for Fibonacci sequence:"))
a, b = 0, 1
print("Fibonacci sequence:")
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b

#4 To find the largest of three numbers
num1= int(input("Enter the first number:"))
num2= int(input("Enter the second number:"))
num3= int(input("Enter the third number:"))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print("The largest number is:", largest)

#5 Create Student Result system- a. Input Student Details b.Input marks c. Display Grades using if else loop n while loop
# Student Result System
name = input("Enter the student's name:")
eng = int(input("Enter marks for English:"))

maths = int(input("Enter marks for Maths:"))
science = int(input("Enter marks for Science:"))
total = eng + maths + science
percentage = (total / 300) * 100
if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)


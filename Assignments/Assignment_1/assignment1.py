#ASSIGNMENT 1
# Q1: Find the area of rectangle
length = int(input("enter length of rectangle:"))
breadth = int(input("enter breadth of rectangle:"))
area = length*breadth
print("area of rectangle is:", area)
# Q2: Find simple interest
p=int(input("enter principal amount:"))
r=int(input("enter rate of interest:"))
t=int(input("enter time in years:"))
s=(p*r*t)/100
print("simple interest is:", s)
# Q3: Convert temperature from Celsius to Fahrenheit
c=int(input("enter temperature in celsius:"))
f=(c*9/5)+32
print("temperature in fahrenheit is:", f)
# Q4: Find the average of three numbers
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
average=(a+b+c)/3
print("average of three numbers is:", average)
# Q5: Find the square and cube of the number
num=int(input("enter a number:"))
print("square of the number is:", num**2)
print("cube of the number is:", num**3)
# Q6: Swap two numbers without third variable
x=int(input("enter first number:"))
y=int(input("enter second number:"))
x,y=y,x
print("after swapping, first number is:", x)
print("after swapping, second number is:", y)
# Q7: Student Report Program

# Taking student details as input
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Taking marks as input
marks1 = float(input("Enter marks for Subject 1: "))
marks2 = float(input("Enter marks for Subject 2: "))
marks3 = float(input("Enter marks for Subject 3: "))
marks4 = float(input("Enter marks for Subject 4: "))
marks5 = float(input("Enter marks for Subject 5: "))

# Calculating total marks
total = marks1 + marks2 + marks3 + marks4 + marks5

# Calculating percentage
percentage = (total / 500) * 100

# Displaying student report
print("\n----- STUDENT REPORT -----")
print("Name :", name)
print("Roll No. :", roll_no)
print("Total Marks :", total)
print("Percentage :", percentage, "%")

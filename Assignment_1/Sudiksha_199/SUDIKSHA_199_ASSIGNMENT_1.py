
#Assignment 1

#1
#Let a and b be respectively the length and breadth of the rectangle

a = int(input("Enter the length: "))
b = int(input("Enter the breadth: "))

area = a*b

print("Area of rectangle: ", area)


#2
#Let p,r and t be the principle amount, rate of interest and time respectively

p = 10000
r = 12
t = 2

#Let s be the simple interest
s = p*r*t

print("Simple Interest for respective data would be: ", s)


#3
#Let c be temperature in celsius and f in fahrenheit

c = float(input("Enter the temperature: "))
f = (c*9/5) + 32

print("Temperature in Fahrenheit: ", f)


#4
#x,y and z be the 3 numbers

x = 2
y = 3
z = 5

avg = (x+y+z)/3

print("Average of Given 3 numbers: ", avg)


#5
#Let m be the number and s be square of m and c be the cube of m

m = int(input("Enter the number: "))
c = m**3
s = m**2

print("Square of the number: ", s)
print("Cube of the number: ", c)


#6
#Let x and y be the two numbers

x = int(input("Enter the first Number: "))
y = int(input("Enter the second Number: "))

x = x+y
x = x-y
y = x-y

print("x=", x)
print("y=", y)


#7
#let m be the marks of students

# Student Report Program

# Taking student details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Taking marks of 3 subjects
marks1 = float(input("Enter marks of Subject 1: "))
marks2 = float(input("Enter marks of Subject 2: "))
marks3 = float(input("Enter marks of Subject 3: "))

# Calculating total marks
total = marks1 + marks2 + marks3

# Calculating percentage
percentage = (total / 300) * 100

# Displaying report
print("\n----- STUDENT REPORT -----")
print("Name:", name)
print("Roll Number:", roll_no)
print("Subject 1 Marks:", marks1)
print("Subject 2 Marks:", marks2)
print("Subject 3 Marks:", marks3)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
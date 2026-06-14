# Program to find area of a rectangle

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth

print("Area of Rectangle =", area)

# Program to calculate Simple Interest

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (in years): "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)


# Program to find average of three numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print("Average =", average)


# Program to find square and cube of a number

num = int(input("Enter a number: "))

square = num ** 2
cube = num ** 3

print("Square =", square)
print("Cube =", cube)


# Program to swap two numbers without using a third variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before Swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After Swapping:")
print("a =", a)
print("b =", b)



# Student Report Program

# Taking student details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Taking marks of 3 subjects
marks1 = float(input("Enter marks in Subject 1: "))
marks2 = float(input("Enter marks in Subject 2: "))
marks3 = float(input("Enter marks in Subject 3: "))

# Calculating total marks
total = marks1 + marks2 + marks3

# Calculating percentage
percentage = (total / 300) * 100

# Displaying report
print("\n===== STUDENT REPORT =====")
print("Student Name :", name)
print("Roll Number  :", roll_no)
print("Subject 1 Marks :", marks1)
print("Subject 2 Marks :", marks2)
print("Subject 3 Marks :", marks3)
print("Total Marks  :", total)
print("Percentage   :", percentage, "%")

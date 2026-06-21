length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth

print("Area of Rectangle =", area)
p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time (years): "))

si = (p * r * t) / 100

print("Simple Interest =", si)
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (9/5) * celsius + 32

print("Temperature in Fahrenheit =", fahrenheit)
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

average = (a + b + c) / 3

print("Average =", average)
num = int(input("Enter a number: "))

square = num ** 2
cube = num ** 3

print("Square =", square)
print("Cube =", cube)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After Swapping:")
print("a =", a)
print("b =", b)
# Student Report Program

# Input student details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Input marks
m1 = float(input("Enter marks in Subject 1: "))
m2 = float(input("Enter marks in Subject 2: "))
m3 = float(input("Enter marks in Subject 3: "))

# Calculate total and percentage
total = m1 + m2 + m3
percentage = total / 3

# Display Report
print("\n------ STUDENT REPORT ------")
print("Name       :", name)
print("Roll No    :", roll_no)
print("Subject 1  :", m1)
print("Subject 2  :", m2)
print("Subject 3  :", m3)
print("Total Marks:", total)
print("Percentage :", percentage, "%")
# area of rectangle
length = 7
width = 10
area = length * width
print("Area of rectangle:", area)

# simple interest
principal = 1000
rate = 6
time = 4
simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)

# convert temperature from Celsius to Fahrenheit
celsius = int(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# Calculate average of three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print("Average of three numbers:", average)

# Find square and cube of a number
number = int(input("Enter a number: "))
square = number ** 2
cube = number ** 3
print("Square of the number:", square)
print("Cube of the number:", cube)

# swap two numbers without third variable
a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
print("Before swapping:")
print("a =", a)
print("b =", b)
a = a + b
b = a - b
a = a - b
print("After swapping:")
print("a =", a)
print("b =", b)

# Create a Student Report Program
name = input("Enter student's name: ")
roll_number = input("Enter roll number: ")
course_name = input("Enter course name: ")
Maths_marks = float(input("Enter maths marks: "))
Science_marks = float(input("Enter science marks: "))
History_marks = float(input("Enter history marks: "))
print("\nStudent Report")
print("Name:", name)
print("Roll Number:", roll_number)
print("Course Name:", course_name)
print("Maths Marks:", Maths_marks)
print("Science Marks:", Science_marks)
print("History Marks:", History_marks)
Total = Maths_marks + Science_marks + History_marks
percentage = (Total / 300) * 100
print("Total Marks:", Total)
print("Percentage:", percentage, "%")
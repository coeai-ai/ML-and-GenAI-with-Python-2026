
# -------------------------------
# Python Assignment-1 Solution
# -------------------------------

# 1. Area of Rectangle
print("1. Area of Rectangle")
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
area = length * width
print("Area of Rectangle =", area, "square units")

# 2. Simple Interest
print("\n2. Simple Interest")
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest (%): "))
time = float(input("Enter time (years): "))

simple_interest = (principal * rate * time) / 100
print("Simple Interest =", simple_interest)

# 3. Celsius to Fahrenheit
print("\n3. Celsius to Fahrenheit")
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(celsius, "°C =", fahrenheit, "°F")

# 4. Average of Three Numbers
print("\n4. Average of Three Numbers")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3
print("Average =", average)

# 5. Square and Cube of a Number
print("\n5. Square and Cube of a Number")
num = float(input("Enter a number: "))

square = num ** 2
cube = num ** 3

print("Square =", square)
print("Cube =", cube)

# 6. Swap Two Numbers Without Third Variable
print("\n6. Swap Two Numbers Without Third Variable")
a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))

print("Before Swap:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After Swap:")
print("a =", a)
print("b =", b)

# 7. Student Report Program
print("\n7. Student Report Program")

name = input("Enter Student Name: ")
rollno = input("Enter Roll Number: ")

english = float(input("Enter English Marks: "))
maths = float(input("Enter Maths Marks: "))
science = float(input("Enter Science Marks: "))
hindi = float(input("Enter Hindi Marks: "))
computer = float(input("Enter Computer Marks: "))

total_marks = english + maths + science + hindi + computer
max_marks = 500
percentage = (total_marks / max_marks) * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F (Fail)"

print("\nSTUDENT REPORT CARD")

print("Student Details")
print("Name        :", name)
print("Roll Number :", rollno)

print("\nMarks Obtained")
print("English     :", english)
print("Maths       :", maths)
print("Science     :", science)
print("Hindi       :", hindi)
print("Computer    :", computer)

print("\nResult")
print("Total Marks :", total_marks, "/", max_marks)
print("Percentage  :", round(percentage, 2), "%")
print("Grade       :", grade)

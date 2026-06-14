length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
print(f"The area of the rectangle is: {area}")

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (%): "))
time = float(input("Enter the time period (in years): "))

simple_interest = (principal * rate * time) / 100
print(f"The Simple Interest is: {simple_interest}")

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3
print(f"The average of the three numbers is: {average}")

number = float(input("Enter a number: "))

square = number ** 2
cube = number ** 3

print(f"Square: {square}")
print(f"Cube: {cube}")

a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))

a, b = b, a

print("\nAfter swapping:")
print(f"a = {a}")
print(f"b = {b}")


student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")

math_marks = float(input("Enter marks for Mathematics: "))
science_marks = float(input("Enter marks for Science: "))
english_marks = float(input("Enter marks for English: "))

total_marks = math_marks + science_marks + english_marks
percentage = (total_marks / 300) * 100

print("\n" + "="*30)
print("         REPORT CARD        ")
print("="*30)
print(f"Name:        {student_name}")
print(f"Roll No:     {roll_number}")
print("-"*30)
print(f"Total Marks: {total_marks} / 300")
print(f"Percentage:  {percentage:.2f}%")
print("="*30)
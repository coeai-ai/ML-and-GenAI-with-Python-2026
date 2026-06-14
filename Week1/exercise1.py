# 1.) Find the area of rectangle 
 
length = 6
breath = 2
print(f"The area of triangle of length :{length} and breath :{breath} is {length*breath}")

# 2.) Find the simple interest

principle_value = 1000
rate_of_interest = 5
time = 3

SI = principle_value * rate_of_interest * time / 100
print(f"The simple interest is : ${SI}")

# 3.) Convert the temperature from Celsius to Fahrenheit
cel = 38
convert = 1.8 * cel + 32

print(f"Converting {cel} celsius to Fahrenheit {convert} Fahrenheit")

# 4.) Calculate average of 3 numbers.
# Calculate average of 3 numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print("Average =", average)

# 5.) Find square and cube of a number.
# Find square and cube of a number

num = int(input("Enter a number: "))

square = num ** 2
cube = num ** 3

print("Square =", square)
print("Cube =", cube)

# 6.) Swap two numbers without third variable.
# Swap two numbers without third variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

# 7.) Create a Student Report Program that take student details using input(), Store marks in variables, Calculate total and percentage , Use comments, Use proper indentation
# Student Report Program

# Input student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Input marks
maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))

# Calculate total marks
total = maths + science + english

# Calculate percentage
percentage = total / 3

# Display report
print("\n----- Student Report -----")
print("Name:", name)
print("Roll Number:", roll_no)
print("Maths:", maths)
print("Science:", science)
print("English:", english)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
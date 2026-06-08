#ASSIGNMENT 1

# 1. Find Area of Rectangle
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print("Area of Rectangle =", area)


# 2. Find Simple Interest
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (in years): "))
simple_interest = (principal * rate * time) / 100
print("Simple Interest =", simple_interest)


# 3. Celsius to Fahrenheit Conversion
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit =", fahrenheit)


# 4. Average of 3 Numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print("Average =", average)


# 5. Square and Cube of a Number
number = int(input("Enter a number: "))
square = number ** 2
cube = number ** 3
print("Square =", square)
print("Cube =", cube)


# 6. Swap Two Numbers Without Third Variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print("After Swapping:")
print("a =", a)
print("b =", b)


# 7. Student Report Program
student_name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")
mark1 = float(input("Enter marks of Subject 1: "))
mark2 = float(input("Enter marks of Subject 2: "))
mark3 = float(input("Enter marks of Subject 3: "))
mark4 = float(input("Enter marks of Subject 4: "))
mark5 = float(input("Enter marks of Subject 5: "))
total_marks = mark1 + mark2 + mark3 + mark4 + mark5
percentage = (total_marks / 500) * 100
if percentage >= 40:
    result = "PASS"
else:
    result = "FAIL"

print("\n----- STUDENT REPORT -----")
print("Student Name :", student_name)
print("Roll Number  :", roll_number)
print("Total Marks  :", total_marks)
print("Percentage   :", percentage, "%")
print("Result       :", result)


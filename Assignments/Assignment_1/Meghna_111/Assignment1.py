#ASSIGNMENT 1
#1.Find Area of Rectangle
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

area = length * width

print("Area of Rectangle =", area)

#2. Find Simple Interest
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time: ")) #in years we would enter the time.

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)

#3. Convert Temperature from Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit =", fahrenheit)

#4. Calculate Average of 3 Numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print("Average =", average)

#5. Find Square and Cube of a Number
number = int(input("Enter a number: "))

square = number ** 2
cube = number ** 3

print("Square =", square)
print("Cube =", cube)

#6. Swap Two Numbers Without Using Third Variable
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("\nBefore Swapping")
print("First Number =", num1)
print("Second Number =", num2)

# Swapping logic
num1, num2 = num2, num1

print("\nAfter Swapping")
print("First Number =", num1)
print("Second Number =", num2)

#7.Student Report Program
# Taking student information
student_name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")

# Taking marks of 5 subjects
mark1 = float(input("Enter marks of Subject 1: "))
mark2 = float(input("Enter marks of Subject 2: "))
mark3 = float(input("Enter marks of Subject 3: "))
mark4 = float(input("Enter marks of Subject 4: "))
mark5 = float(input("Enter marks of Subject 5: "))

# Calculating total marks
total_marks = mark1 + mark2 + mark3 + mark4 + mark5

# Calculating percentage
percentage = (total_marks / 500) * 100

# Displaying report
print("\n========== STUDENT REPORT ==========")
print("Student Name :", student_name)
print("Roll Number  :", roll_number)

print("\nMarks Obtained")
print("Subject 1 :", mark1)
print("Subject 2 :", mark2)
print("Subject 3 :", mark3)
print("Subject 4 :", mark4)
print("Subject 5 :", mark5)

print("\nTotal Marks :", total_marks)
print("Percentage  :", percentage, "%")

# Determining Grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"

print("Grade       :", grade)
print("====================================")
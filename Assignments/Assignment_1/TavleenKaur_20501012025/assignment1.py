# 1. area of rectangle
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
area = length * breadth
print("Area of Rectangle =", area)

# 2. simple interest
principal = float(input("\nEnter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (years): "))
simple_interest = (principal * rate * time) / 100
print("Simple Interest =", simple_interest)

# 3. Celsius to Fahrenheit
celsius = float(input("\nEnter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit =", fahrenheit)

# 4. average of 3 numbers
num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print("Average =", average)

# 5. square and cube
number = float(input("\nEnter a number: "))
square = number ** 2
cube = number ** 3
print("Square =", square)

# 6. swap without third variable
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
print("Before Swapping:")
print("a =", a)
print("b =", b)
a, b = b, a
print("After Swapping:")
print("a =", a)
print("b =", b)

# 7. Student Report Program

# Taking student details
student_name = input("\nEnter Student Name: ")
roll_number = input("Enter Roll Number: ")
# Taking marks
subject1 = float(input("Enter marks in Subject 1: "))
subject2 = float(input("Enter marks in Subject 2: "))
subject3 = float(input("Enter marks in Subject 3: "))
# Calculating total
total_marks = subject1 + subject2 + subject3
# Calculating percentage
percentage = (total_marks / 300) * 100
# Displaying report
print("\n----- STUDENT REPORT -----")

print("Student Name:", student_name)
print("Roll Number:", roll_number)
print("Subject 1 Marks:", subject1)
print("Subject 2 Marks:", subject2)
print("Subject 3 Marks:", subject3)
print("Total Marks:", total_marks)
print("Percentage:", percentage, "%")
#find area of rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print("The area of the rectangle is:", area)
 
 # find simple interest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
simple_interest = (principal * rate * time) / 100
print("The simple interest is:", simple_interest)

#convert temperature from Celsius to Fahrenheit
celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("The temperature in Fahrenheit is:", fahrenheit)

#calculate avg of three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
average = (num1 + num2 + num3) / 3
print("The average of the three numbers is:", average)

#find square and cube of a number
number = float(input("Enter a number: "))
square = number ** 2
cube = number ** 3
print("The square of the number is:", square)
print("The cube of the number is:", cube)

#swap two numbers without third variable
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
a = a + b
b = a - b
a = a - b
print("After swapping, the first number is:", a)
print("After swapping, the second number is:", b)

#student report card
# --- Step 1: Input Student Details & Marks ---
name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

# Convert inputs to integers to allow math calculations
math = int(input("Enter Math marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

# --- Step 2: Calculations ---
total = math + science + english
percentage = (total / 300) * 100

# --- Step 3: Display Results ---
print("\n--- REPORT CARD ---")
print(f"Name: {name} | Roll No: {roll}")
print(f"Total Marks: {total} / 300")
print(f"Percentage: {percentage:.2f}%")

# Proper indentation used for the conditional check
if percentage >= 40:
    print("Status: PASSED")
else:
    print("Status: FAILED")

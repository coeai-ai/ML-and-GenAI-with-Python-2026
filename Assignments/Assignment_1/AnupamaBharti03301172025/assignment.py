# Question1

# Taking three numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
# Calculating average
average = (num1 + num2 + num3) / 3
# Displaying result
print("Average =", average)

#Question2

# Taking principal, rate and time from user
p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time (years): "))
# Calculating simple interest
si = (p * r * t) / 100
# Displaying result
print("Simple Interest =", si)

#Question3

# Taking temperature in Celsius
Celsius = float(input("Enter temperature in Celsius: "))
# Converting to Fahrenheit
Fahrenheit = (Celsius * 9/5) + 32
# Displaying result
print("Temperature in Fahrenheit =", Fahrenheit)

#Question4

# Taking three numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
# Calculating average
average = (num1 + num2 + num3) / 3
# Displaying result
print("Average =", average)

#Question5

# Taking a number from user
num = int(input("Enter a number: "))
# Calculating square and cube
square = num ** 2
cube = num ** 3
# Displaying results
print("Square =", square)
print("Cube =", cube)

#Question6

# Taking two numbers from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
# Swapping values without third variable
a, b = b, a
# Displaying swapped values
print("After Swapping:")
print("a =", a)
print("b =", b)

#Question7

# Taking student details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
# Taking marks for subjects
maths = float(input("Enter Maths Marks: "))
science = float(input("Enter Science Marks: "))
english = float(input("Enter English Marks: "))
# Calculating total and percentage
total = maths + science + english
percentage = total / 3
# Displaying student report
print()
print("----- Student Report -----")
print("Name of the Student:", name)
print("Roll Number of the Student:", roll_no)
print("Total Marks :", total)
print("Percentage :", percentage, "%")

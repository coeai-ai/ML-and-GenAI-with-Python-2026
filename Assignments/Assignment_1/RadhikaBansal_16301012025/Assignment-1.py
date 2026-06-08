
# 1. Find area of rectangle
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print("Area of rectangle =", area)

# 2. Find simple interest
p = float(input("Enter principal amount: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
si = (p * r * t) / 100
print("Simple Interest =", si)

# 3. Convert temperature from Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("Temperature in Fahrenheit =", fahrenheit)

# 4. Calculate average of 3 numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
average = (a + b + c) / 3
print("Average =", average)

# 5. Find square and cube of a number
num = float(input("Enter a number: "))
square = num * num
cube = num * num * num
print("Square =", square)
print("Cube =", cube)


# 6. Swap two numbers without third variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a = a + b
b = a - b
a = a - b
print("After swapping:")
print("a =", a)
print("b =", b)

# 7. Student Report Program

# Input student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Input marks
m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))

# Calculate total
total = m1 + m2 + m3

# Calculate percentage
percentage = total / 3

# Display report
print("\n----- Student Report -----")
print("Name:", name)
print("Roll No:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage, "%")


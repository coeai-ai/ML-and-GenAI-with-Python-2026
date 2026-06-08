#1. Find Area of Rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area of Rectangle =", area)

#2. Find Simple Interest
#Formula: SI = (P × R × T) / 100

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (years): "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)

#3. Convert Temperature from Celsius to Fahrenheit
#Formula: F = (C × 9/5) + 32

celsius = float(input("Enter Temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit =", fahrenheit)


#4. Calculate Average of 3 Numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print("Average =", average)


#5. Find Square and Cube of a Number
num = int(input("Enter a number: "))

square = num ** 2
cube = num ** 3

print("Square =", square)
print("Cube =", cube)

#6. Swap Two Numbers Without Third Variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before Swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After Swapping:")
print("a =", a)
print("b =", b)


#7. Student Report Program



name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
maths = float(input("Enter Maths Marks: "))
science = float(input("Enter Science Marks: "))
english = float(input("Enter English Marks: "))

total = maths + science + english
percentage = (total / 300) * 100


print("\n------ STUDENT REPORT ------")
print("Student Name :", name)
print("Roll Number  :", roll_no)
print("Maths Marks  :", maths)
print("Science Marks:", science)
print("English Marks:", english)
print("Total Marks  :", total)
print("Percentage   :", percentage, "%")
# Student Name: Prachi Bhardwaj
# Enrollment Number: 09301182025
# College Name: IGDTUW

#  ASSIGNMENT 1



#1)Find Area of Rectangle
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth

print("Area of Rectangle =", area)


#2) Find Simple Interest

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (in years): "))

si = (principal * rate * time) / 100

print("Simple Interest =", si)


#3)Convert Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit =", fahrenheit)


#4) Calculate Average of 3 Numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print("Average =", average)


#5) Find Square and Cube of a Number

num = float(input("Enter a number: "))

square = num ** 2
cube = num ** 3

print("Square =", square)
print("Cube =", cube)


#6) Swap Two Numbers Without Third Variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)



#7) Student Report Program

# Taking student details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Taking marks
maths = float(input("Enter Maths Marks: "))
science = float(input("Enter Science Marks: "))
english = float(input("Enter English Marks: "))

# Calculating total and percentage
total = maths + science + english
percentage = (total / 300) * 100


# Displaying report
print("\n----- STUDENT REPORT -----")
print("Name :", name)
print("Roll No :", roll_no)
print("Maths :", maths)
print("Science :", science)
print("English :", english)
print("Total Marks :", total)
print("Percentage :", percentage, "%")
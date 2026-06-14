#ques-1. find area of rectangle
length=13
breadth=17
area=length*breadth
print("area of the rectangle is: ",area)

#ques-2. find simple intrest
principle=5000
rate=12
intrest=5
simple_intrest=(principle*rate*intrest)/100
print("S.I. is: ",simple_intrest)

#ques-3. Celsius to Fahrenheit
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("Temperature in Fahrenheit =", f)

#ques-4. average of 3 numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
avg = (a + b + c) / 3
print("Average =", avg)

#ques-5. square and cube of a number
num = int(input("Enter a number: "))
square = num ** 2
cube = num ** 3
print("Square =", square)
print("Cube =", cube)

#ques-6. swap two numbers without third variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)




#ques-7. student report program

# Student Details

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Marks Input

m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))

# Total and Percentage

total = m1 + m2 + m3
percentage = total / 3

# Report

print("\n----- Student Report -----")
print("Name:", name)
print("Roll No:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
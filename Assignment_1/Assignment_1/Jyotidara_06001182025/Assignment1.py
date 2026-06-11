# area of a rectangle
length = 5
width = 10
Area = length*width
print("area of rectangle = ",Area)

# Simple Interest
p = 10000  # initial amount
r = 10     # Rate of interest per year
t = 2      # Time(year)

Simple_interset = (p*r*t)/100
print("Simple interest is = ",Simple_interset)

# Convert temperature from Celsius to Fahrenheit
celsius = float(input("celsius = "))
Fahrenheit = 1.8*celsius+32
print(Fahrenheit)

# Average of 3 numbers
a = int(input("first number a = "))
b = int(input("second number b = "))
c = int(input("thrid number c = "))

Average = (a+b+c)/3
print(Average)

# square and cube of a number
num = int(input("number = "))
square = num*num
cube = num*num*num
print(square)
print(cube)

# Swaping of two number without using third variable
a = 5
b = 10
a = a+b
b = a - b
a = a - b
print(a)
print(b)

# Student report programm
Student_name = str(input("Student name : "))
Roll_No = float(input("Roll No : "))

print("Marks : ")

Sub1 = float(input("Subject1 : "))
Sub2 = float(input("subject2 : "))
Sub3 = float(input("Subject3 : "))

total = Sub1+Sub2+Sub3
persent = (total/300)*100

print("Total no : ",total,"\nPersent : ",persent)

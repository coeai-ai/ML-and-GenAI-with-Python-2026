#1. Area of rectangle :
length=int(input("Enter the length of rectangle"))
width=int(input("Enter the width of rectangle "))
area=length*width
print("Area of rectangle is ",area)

#2.Simple interest

p=int(input("Enter principle amount"))
r=int(input("Enter rate of interest"))
t=int(input("Enter time period"))
si=(p*r*t)/100
print("simple interst is ",si)

#3. Convert celsius to fahrenheit
c=int(input("Enter the temprature in celsius"))
f=(c*9/5)+32
print("The temprature in fahrenheit is",f)

#4. Average of 3 numbers
x=int(input("Enter 1st number"))
y=int(input("Enter 2nd number"))
z=int(input("Enter 3rd number"))

av=(x+y+z)/3
print("The average is ",av)

#4. Square and cube of the number

n=int(input("Enter a number"))
sq=n*n
print("Square is ",sq)
cube=n**3
print("Cube is ",cube)


# 5.Swap two numbers without third variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

# 6.Student Report Program

# Taking student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Taking marks of 5 subjects
m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))

# Calculating total marks
total = m1 + m2 + m3 + m4 + m5

# Calculating percentage
percentage = total / 5

# Displaying report
print("----- Student Report -----")
print("Name       :", name)
print("Roll No.   :", roll_no)
print("Total Marks:", total)
print("Percentage :", percentage, "%")



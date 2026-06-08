#Assignment 1

#1 Find Area of a rectangle
l=int(input("Enter length of the rectangle:"))
b=int(input("Enter breadth of the rectangle:"))
a=l*b
print("Area of the rectangle=",a)

#2 Find simple interest
principal=float(input("Enter principal amount:"))
rate=float(input("Enter rate in percentage:"))
time=float(input("Enter time in years:"))
simple_interest=(principal*rate*time)/100
print("Simple interest is : ", simple_interest)


#3 Convert temperature from celcius to fahrenheit
c=float(input("Enter temperature in celcius:"))
f=(c*9/5)+32
print(f"Temperature in fahrenheit is : {f}")


#4 Calculate average of three numbers
n1=float(input("Enter first number:"))
n2=float(input("Enter second number:"))
n3=float(input("Enter third number:"))
avg=(n1+n2+n3)/3
print("Required average: ", avg)

#5 Find square and cube of a number
num=float(input("Enter number:"))
sq=num**2
cu=num**3
print(f"Square: {sq}, Cube: {cu}")

#6 Swap two numbers without third variable
a=int(input("Enter first number (a):"))
b=int(input("Enter second number(b):"))
print(f"Before swap: a={a},b={b}")
a,b=b,a
print(f"After swap: a={a},b={b}")

#7 Student report programme

#Taking student details
name=input("Enter name:")
age=input("Enter age:")
grade=input("Enter grade:")
#Storing marks in variables
phy_marks=float(input("Enter physics marks:"))
math_marks=float(input("Enter mathematics marks:"))
bio_marks=float(input("Enter biology marks:"))
chem_marks=float(input("Enter chemistry marks:"))
eng_marks=float(input("Enter english marks:"))
#Calculate total and percentage
total=phy_marks+math_marks+bio_marks+eng_marks+chem_marks
p=total/5
print("Total Marks=",total)
print("Percentage=",p)
















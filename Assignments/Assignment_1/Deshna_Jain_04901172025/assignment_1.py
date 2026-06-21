# 1. Find area of rectangle
length=float(input("Enter length:"))
breadth=float(input("Enter breadth:"))
print("Area:",length*breadth)


# 2. Find simple interest
p=float(input("Enter principal:"))
r=float(input("Enter rate:"))
t=float(input("Enter time:"))
print("Simple Interest:",p*r*t/100)


# 3. Convert Celsius to Fahrenheit
c=float(input("Enter temperature in Celsius:"))
print("Fahrenheit:",c*9/5+32)


# 4. Calculate average of 3 numbers
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
c=float(input("Enter third number:"))
print("Average:",(a+b+c)/3)


# 5. Find square and cube
n=int(input("Enter number:"))
print("Square:",n*n)
print("Cube:",n*n*n)


# 6. Swap two numbers without third variable
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
a=a+b
b=a-b
a=a-b
print("After swap:",a,b)


# 7. Student report program
name=input("Enter name:")
roll=input("Enter roll number:")
m1=float(input("Enter marks 1:"))
m2=float(input("Enter marks 2:"))
m3=float(input("Enter marks 3:"))
total=m1+m2+m3
print("Total:",total)
print("Percentage:",total/300*100)
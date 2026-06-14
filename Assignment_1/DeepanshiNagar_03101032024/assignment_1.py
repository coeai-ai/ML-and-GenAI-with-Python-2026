#1
len = float(input("enter length:"))
breadth = float(input("enter breadth:"))
area = len*breadth
print("area =", area)

#2
p = float(input("enter principal:"))
r = float(input("enter Rate:"))
t = float(input("enter Time:"))
si = (p*r*t)/100
print("simple interest:", si)

#3
c = float(input("Enter Temperature in Celsius: "))
f = (c * 9/5) + 32
print("Temperature in Fahrenheit =", f)

#4
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
avg = (a + b + c) / 3
print("Average =", avg)

#5
n = int(input("Enter a number: "))
print("Square =", n ** 2)
print("Cube =", n ** 3)

#6
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print("After Swapping:")
print("a =", a)
print("b =", b)

#7
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))

total = m1 + m2 + m3
percentage = total / 3

print("\n----- Student Report -----")
print("Name :", name)
print("Roll No :", roll_no)
print("Total Marks :", total)
print("Percentage :", percentage, "%")



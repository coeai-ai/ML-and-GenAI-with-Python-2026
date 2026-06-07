# 1. Area of Rectangle
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print("Area of Rectangle =", area)

# 2. Simple Interest
p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))
si = (p * r * t) / 100
print("Simple Interest =", si)

# 3. Celsius to Fahrenheit
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("Temperature in Fahrenheit =", f)

# 4. Average of 3 Numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
avg = (a + b + c) / 3
print("Average =", avg)

# 5. Square and Cube
n = int(input("Enter a number: "))
print("Square =", n**2)
print("Cube =", n**3)

# 6. Swap without Third Variable
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

x = x + y
y = x - y
x = x - y

print("After Swapping")
print("x =", x)
print("y =", y)

# 7. Student Report Program
name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

m1 = float(input("Enter Marks 1: "))
m2 = float(input("Enter Marks 2: "))
m3 = float(input("Enter Marks 3: "))

total = m1 + m2 + m3
percentage = total / 3

print("\n----- STUDENT REPORT -----")
print("Name:", name)
print("Roll Number:", roll)
print("Total Marks:", total)
print("Percentage:", percentage)
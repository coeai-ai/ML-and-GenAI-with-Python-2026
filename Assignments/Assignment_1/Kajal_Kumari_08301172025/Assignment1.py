# 1.Find area of rectangle. 
length = float(input("Enter length:"))
breadth = float(input("Enter breadth:"))
area = length * breadth
print("Rectangle area:", area)

# 2.Find simple interest
p = float(input("Enter principal:"))
r = float(input("Enter Rate:"))
t = float(input("Enter time:"))
si = (p * r * t) / 100
print("Simple Interest is:", si)

# 3.Convert temperature from celsius to fahrenheit
celsius = float(input("Enter temperature in celsius:"))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in fahrenheit", fahrenheit)

# 4.Calculate average of 3 numbers. 
a = float(input("Enter a:"))
b = float(input("Enter b:"))
c = float(input("Enter c:"))
average = (a + b + c) / 3
print("Average:", average)


# 5.Find square and cube of a number. 
a = int(input("Enter the number:"))
square = a**2
cube = a **3
print("Square =", square)
print("Cube =", cube)



# 6. Swap two numbers without third variable
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
a, b = b, a
print("a and b are :", a, b)


# 7.Create a Student Report Program that take student details using input(), 
# Store marks in variables, Calculate total and percentage , Use comments, Use proper indentation
Name = input("Enter Student name:")
roll_no = input("Enter roll number:")
Maths = float(input("Enter Marks:"))
Physics = float(input("Enter Marks:"))
Chemistry = float(input("Enter Marks:"))
English = float(input("Enter Marks:"))
PHE = float(input("Enter Marks:"))
Total = Maths + Physics + Chemistry + English + PHE
percentage = Total / 5
print("Student Report")
print("Name:", Name)
print("Roll Number:", roll_no)
print("Total Marks:", Total)
print("Percentage:", percentage, "%")


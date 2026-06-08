
# 1. FIND AREA OF RECTANGLE

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth

print("Area of Rectangle =", area)


# 2. FIND SIMPLE INTEREST

principal = float(input("\nEnter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (Years): "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)


# 3. CONVERT CELSIUS TO FAHRENHEIT

celsius = float(input("\nEnter Temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit =", fahrenheit)


# 4. CALCULATE AVERAGE OF 3 NUMBERS

num1 = float(input("\nEnter First Number: "))
num2 = float(input("Enter Second Number: "))
num3 = float(input("Enter Third Number: "))

average = (num1 + num2 + num3) / 3

print("Average =", average)


# 5. FIND SQUARE AND CUBE OF A NUMBER

number = int(input("\nEnter a Number: "))

square = number ** 2
cube = number ** 3

print("Square =", square)
print("Cube =", cube)


# 6. SWAP TWO NUMBERS WITHOUT THIRD VARIABLE

a = int(input("\nEnter First Number: "))
b = int(input("Enter Second Number: "))

a = a + b
b = a - b
a = a - b

print("After Swapping:")
print("a =", a)
print("b =", b)


# 7. STUDENT REPORT PROGRAM

# Taking student details
name = input("\nEnter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Taking marks
mark1 = float(input("Enter Marks in Subject 1: "))
mark2 = float(input("Enter Marks in Subject 2: "))
mark3 = float(input("Enter Marks in Subject 3: "))

# Calculating total and percentage
total = mark1 + mark2 + mark3
percentage = (total / 300) * 100

# Displaying report
print("\n========== STUDENT REPORT ==========")
print("Student Name :", name)
print("Roll Number  :", roll_no)
print("Subject 1 Marks :", mark1)
print("Subject 2 Marks :", mark2)
print("Subject 3 Marks :", mark3)
print("Total Marks :", total)
print("Percentage  :", percentage, "%")
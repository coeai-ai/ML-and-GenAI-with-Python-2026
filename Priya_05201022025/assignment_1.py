# Program 1: Area of Rectangle

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print("Area of Rectangle =", area)


# Program 2: Simple Interest

principal = float(input("\nEnter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (in years): "))
simple_interest = (principal * rate * time) / 100
print("Simple Interest =", simple_interest)


# Program 3: Celsius to Fahrenheit

celsius = float(input("\nEnter Temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit =", fahrenheit)


# Program 4: Average of Three Numbers

num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print("Average =", average)


# Program 5: Square and Cube

number = int(input("\nEnter a number: "))
print("Square =", number ** 2)
print("Cube=", number ** 3)


# Program 6: Swap Two Numbers

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print("After Swapping:")
print("First Number=", a)
print("Second Number=", b)


# Program 7: Student Report Program

student_name = input("\nEnter Student Name: ")
mark1 = float(input("Enter marks of Subject 1: "))
mark2 = float(input("Enter marks of Subject 2: "))
mark3 = float(input("Enter marks of Subject 3: "))
mark4 = float(input("Enter marks of Subject 4: "))
mark5 = float(input("Enter marks of Subject 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5
percentage = total / 5
print("\nSTUDENT REPORT")
print("Student Name:", student_name)
print("Total Marks:", total)
print("Percentage:", round(percentage, 2), "%")

if percentage >= 90:
    print("Grade : A+")
elif percentage >= 80:
    print("Grade : A")
elif percentage >= 70:
    print("Grade : B")
elif percentage >= 60:
    print("Grade : C")
else:
    print("Grade : Fail")
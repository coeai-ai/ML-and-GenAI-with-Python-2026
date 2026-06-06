# ASSIGNMENT:1
#1. Find the area of a rectangle.
length = int(input("Please enter length of rectangle: "))
breadth = int(input("Please enter breadth of rectangle: "))
area = length * breadth
print("Area of the rectangle is: ", area , "sqaure units.")

#2. Find simple interest.
principal = int(input("Enter principal amount: "))
rate = int(input("Enter rate amount: "))
time = int(input("Enter time in years: "))
si = principal * rate * time
print("The simple interest is: " , si)

#3. Convert temperature from celsius to fahrenheit.
celsius = int(input("Enter temperature in celsius: "))
fahrenheit = (celsius)*(9/5)+32
print("The temperature in fahrenheit is: " , fahrenheit)

#4. Compute average of 3 numbers.
numOne = int(input("Enter first number: "))
numTwo = int(input("Enter second number: "))
numThree = int(input("Enter third number: "))
average = (numOne+numTwo+numThree)/3
print("The average is: ",average)

#5. Find square & cube of a number.
num = int(input("Enter a number: "))
square = num**2
cube = num**3
print("The square of the number is: ", square)
print("The cube of the number is: ", cube)

#6. Swap two numbers without using third variable:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a,b)
a = a+b
b = a-b
a = a-b
print(a,b)

#7. Create a Student Report Program that takes student's details using input(), store marks in variables, Calculate Total & Percentage, use comments, and use proper indentation.
name = input("Enter your name: ")
physics = int(input("Enter marks in physics:"))
maths = int(input("Enter marks in maths: "))
chemistry = int(input("Enter marks in chemistry: "))
sum=physics + maths + chemistry
avg = (sum)/3
total = 300
percentage = (sum/total)*100
print("Your total marks out of 300 are: " , total)
print("Your percentage is: " , percentage)

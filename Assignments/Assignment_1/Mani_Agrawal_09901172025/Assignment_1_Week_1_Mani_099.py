# Question 1 - Find area of rectangle
length=float(input("Enter length of the rectangle:"))
breadth=float (input("Enter breadth of the rectange:"))
area=length*breadth
print(f"Area of the rectange is {area}")

# Question 2 - Find simple interest. 
Principal=float(input("Enter principal value:"))
Rate=float(input("Enter interest rate in percent:"))
Time=float(input("Enter time in years:"))
simpleInterest=Principal*Rate*Time/100
print(f"Simple Interest is {simpleInterest}")

# Question 3 - Convert temperature from Celsius to Fahrenheit. 
celsius=float(input("Enter temperature in celsius:"))
farenhiet=celsius*9/5+32
print(f"{celsius} celsius in farenhiet is {farenhiet} farenhiet")

# Question 4 - Calculate average of 3 numbers. 
num1=float(input("Enter value of first number:"))
num2=float(input("Enter value of second number:"))
num3=float(input("Enter value of third number:"))
average=(num1+num2+num3)/3
print(f"Average of number {num1} , {num2} and {num3} is {average}")

# Question 5 - Find square and cube of a number. 
num=int(input("Enter number:"))
square=num**2
cube=num**3
print(f"Square and cube of {num} is {square} and {cube} respectively")

# Question 6 - Swap two numbers without third variable.
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
print("Before swapping")
print(f"First number is {num1} and second number is {num2}")
num1,num2=num2,num1
print("Afte swapping:")
print(f"First number is {num1} and second number is {num2}")

# Question 7 - Create a Student Report Program that take student details using input(), Store marks in variables, Calculate total and percentage , Use comments, Use proper indentation.
# Student Report
# Taking student name, roll no. and his/her 5 subject marks as input
name=input("Enter name of the student:")
rollNo=int(input("Enter roll no.:"))
sub1=float(input("Enter marks of sub1:"))
sub2=float(input("Enter marks of sub2:"))
sub3=float(input("Enter marks of sub3:"))
sub4=float(input("Enter marks of sub4:"))
sub5=float(input("Enter marks of sub5:"))
# Calculating total marks of the student out of 500
totalMarks=sub1+sub2+sub3+sub4+sub5
# Calculating percentage
percentage=totalMarks/500*100
# Printing total marks and percentage of the student
print(f"Total Marks is {totalMarks}")
print(f"Percentage is {percentage} %")

#ASSIGNMENT 1
#Swanandi Garudkar 23301012025
#Indira Gandhi Delhi Technical University for Women

#1. Find area of rectangle.

a=int(input("Enter the length of the rectangle = "))
b=int(input("Enter the breadth of the rectangle = "))
area=a*b
print("Area of the rectangle = ",area)

#2. Find simple interest. 

p=int(input("Enter the principal amount = "))
r=int(input("Enter the rate of interest = "))
t=int(input("Enter the time ( in years ) = "))
si=(p*r*t)/100
print("Simple Interest = ",si)

#3. Convert temperature from Celsius to Fahrenheit. 

c=int(input("Enter the temperature in Celsius = "))
f=(c*9/5)+32
print("Temperature in Farenheit = ",f)

#4. Calculate average of 3 numbers. 

a=int(input("Enter the 1st no. = "))
b=int(input("Enter the 2nd no. = "))
c=int(input("Enter the 3rd no. = "))
av=(a+b+c)/3
print("Average of the 3 no. = ",av)

#5. Find square and cube of a number. 

x=int(input("Enter a no. = "))
print("Square of the no. = ",x*x)
print("Cube of the no. = ",x**3)

#6. Swap two numbers without third variable.

a=int(input("Enter the 1st no. = "))
b=int(input("Enter the 2nd no. = "))
a,b=b,a
print("1st no. = ",a)
print("2nd no. = ",b)

#7. Create a Student Report Program that take student details using input(),
#Store marks in variables, Calculate total and percentage , Use comments,
#Use proper indentation

# Taking student details
name = input("Enter Student Name = ")
rollno = int(input("Enter Roll Number = "))

# Storing marks in variables
math = float(input("Enter Math marks = "))
science = float(input("Enter Science marks = "))
english = float(input("Enter English marks = "))

# Calculating total and percentage (assuming max marks per subject is 100)
total_marks = math + science + english
percentage = (total_marks / 300) * 100

# Printing the report
print("Student Report Card")
print("Name = ", name)
print("Roll No = ", rollno)
print("Total Marks = ", total_marks)
print("Percentage = ", percentage, "%")






















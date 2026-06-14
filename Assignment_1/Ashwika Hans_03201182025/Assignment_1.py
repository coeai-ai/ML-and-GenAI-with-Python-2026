#Student Name : Ashwika Hans
#Enrollment Number : 03201182025
#College Name : Indira Gandhi Delhi Technical University for Women

# Find the area of a rectangle
length = int(input("Enter the length : "))
breadth = int(input("Enter the breadth : "))
area = length * breadth
print("The area of the rectangle is : ", area)

#Find simple interest
principal = int(input("Enter the principal amount : "))
rate = float(input("Enter the rate of interest : "))
time = int(input("Enter the time period : "))
simple_interest = (principal * rate * time) / 100
print("The simple interest is : ", simple_interest)

#Convert Celsius to Fahrenheit
celsius = float(input("Enter the temperature in Celsius : "))
fahrenheit = (celsius * 9/5) + 32
print("The temperature in Fahrenheit is : ", fahrenheit)

#Calculate average of three numbers
num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))   
num3 = float(input("Enter the third number : "))
average = (num1 + num2 + num3) / 3
print("The average of the three numbers is : ", average)

#Find the square and cube of a number
number = int(input("Enter a number : "))
square = number ** 2    
cube = number ** 3
print("The square of the number is : ", square)
print("The cube of the number is : ", cube)

#Swap two numbers without third variable 
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))    
a = a + b
b = a - b
a = a - b
print("After swapping, the first number is : ", a)
print("After swapping, the second number is : ", b)


#Create a student report program that takes student details using input(),stores marks in variables,
#calculates total and percentage, use comments, use proper indentation

# Taking student details
name = input("Enter the student's name : ")
age = int(input("Enter the student's age : "))
grade = input("Enter the student's grade : ")

# Taking marks for three subjects
maths = int(input("Enter the marks for Maths : "))
science = int(input("Enter the marks for Science : "))
english = int(input("Enter the marks for English : "))

# Calculating total marks
total_marks = maths + science + english

# Calculating percentage
percentage = (total_marks / 300) * 100

# Displaying the student report
print("\nStudent Report")
print("Name : ", name)
print("Age : ", age)
print("Grade : ", grade)
print("Total Marks : ", total_marks)
print("Percentage : ", percentage, "%")







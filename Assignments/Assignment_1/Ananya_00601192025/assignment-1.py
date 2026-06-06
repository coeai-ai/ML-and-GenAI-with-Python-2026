#1 Find area of rectangle.
length = 5
breadth = 25
area = length*breadth
print("Area of rectangle is: ", area)


#2 Find simple interest.
principal=1000
rate=7
time=10
simpleint=principal*rate*time/100
print("Simple Interest is: ", simpleint)

#3 Convert temperature from Celsius to Fahrenheit
temp_celsius = 25
temp_fahrenheit = (temp_celsius * 9/5) + 32
print("Temperature in Fahrenheit is: ", temp_fahrenheit)

#4 Calculate average of 3 numbers.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print("average is :" , average)

#Find square and cube of a number.
num=5
print("Square of number is: ", num**2)
print("Cube of number is: ", num**3)

#6 Swap two numbers without third variable.
x=5
y=10
x,y=y,x
print("After swapping: x =", x, "y =", y)



#7 Create a Student Report Program that take student details using input(), Store marks in variables, Calculate total and percentage , Use comments, Use proper indentation
name=input("Enter student name: ")
rollno=int(input("Enter roll number: "))
# Taking marks for three subjects
marks1=int(input("Enter marks for subject 1: ")) 
marks2=int(input("Enter marks for subject 2: "))
marks3=int(input("Enter marks for subject 3: "))
# Calculating total marks and percentage
total = marks1 + marks2 + marks3
percentage = (total / 300) * 100
# Displaying the student report
print("studnt report :")
print("Name: ", name)
print("Roll Number: ", rollno)
print("Total Marks: ", total)
print("Percentage: ", percentage, "%")
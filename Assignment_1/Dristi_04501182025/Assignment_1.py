# To calculate the area of a rectangle
length= 3
breadth= 4
area= length * breadth
print("The area of the rectangle is:", area)

#Q2: To calculate the simple interest
principal= 1000
rate= 5
time= 2
simple_interest= (principal * rate * time) / 100
print("The simple interest is in currency:", simple_interest)

#Q3: Convert temperature from Celsius to Fahrenheit
celsius= 25
fahrenheit= (celsius * 9/5) + 32
print("The temperature in Fahrenheit is:", fahrenheit)

#4: Calculate the average of three numbers
num1= 10
num2= 20
num3= 30
average= (num1 + num2 + num3) / 3
print("The average of the three numbers is:", average)

#5: Find the square and cube of a number
number= 5
square= number ** 2
cube= number ** 3
print("The square of the number is:", square)
print("The cube of the number is:", cube)

#6: Swap the values of two variables without a third variable
a=6
b=4
a,b= b,a
print("After swapping, a is:", a)
print("After swapping, b is:", b)

#7: Create a Student Report Program that take student details using input(), Store marks in variables, Calculate total and percentage , Use comments, Use proper indentation
# Student Report Program

#Create the Students Report:
eng = int(input("Enter marks for English:"))
maths = int(input("Enter marks for Maths:"))
science = int(input("Enter marks for Science:"))
#Calculate total n Percentage:
total = eng+maths+science
percentage = (total/300)*100
#Print the Report:
print("Total Marks:", total)
print("Percentage:", percentage)

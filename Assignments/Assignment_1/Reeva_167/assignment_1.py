
#1.Find the area of a rectangle
length=float(input("Enter the length of the rectangle:"))
width=float(input("Enter the width of the rectangle:"))
area=length*width
print("The area of the rectangle is:",area,"\n")

#2.Find simple interest
principal=float(input("Enter the principal amount:"))
rate=float(input("Enter the rate of interest:"))
time=float(input("Enter the time in years:"))
simple_interest=(principal*rate*time)/100
print("The simple interest is:",simple_interest,"\n")

#3.Convert temperature from Celsius to Fahrenheit
celsius=float(input("Enter the temperature in Celsius:"))
fahrenheit=(celsius*9/5)+32
print("The temperature in Fahrenheit is:",fahrenheit,"\n")

#4.Find the average of three numbers
num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
num3=float(input("Enter the third number:"))
average=(num1+num2+num3)/3
print("The average of the three numbers is:",average,"\n")

#5 Find square and cube of a number
num=float(input("Enter a number:"))
square=num**2
cube=num**3
print("The square of the number is:",square,"\n")
print("The cube of the number is:",cube,"\n")

#6 Swap two numbers without third variable
a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))          
print("Before swapping: num1 =",a,"num2 =",b)
a=a+b
b=a-b
a=a-b
print("After swapping: num1 =",a,"num2 =",b,"\n")


#7 Create a Student Report Program that take student details using input(), Store marks in variables, Calculate total and percentage 
name=input("Enter the student's name:")
roll_num=int(input("Enter roll number:"))
marks1=float(input("Enter marks for subject 1:"))
marks2=float(input("Enter marks for subject 2:"))
marks3=float(input("Enter marks for subject 3:"))
marks4=float(input("Enter marks for subject 4:"))
total=marks1+marks2+marks3+marks4
percentage=(total/400)*100
print("Student Name:",name,"\n")
print("Roll Number:",roll_num,"\n")
print("Total Marks:",total,"\n")
print("Percentage:",percentage,"\n")






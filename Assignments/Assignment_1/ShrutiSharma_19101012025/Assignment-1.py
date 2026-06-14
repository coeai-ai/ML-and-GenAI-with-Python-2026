#ASSIGNMENT-1

#Find area of rectangle

length= int(input("Enter length of rectangle:"))
breadth= int(input("Enter breadth of rectangle:"))
area= length*breadth
print("Area of rectangle is ", area)

#Find simple interest

p= int(input("Enter principal:"))
r= int(input("Enter rate:"))
t= int(input("Enter time:"))
s_i= (p*r*t)/100
print("Simple interest is ", s_i)

#Covert temperature from celsius to fahrenheit

temp1=int(input("Enter temperature in celsius:"))
temp2= (temp1*9)/5 + 32
print ("Temperature in Fahrenheit is ",temp2)

#Calculate average of three number

num1= int(input("Enter First number:"))
num2= int(input("Enter second number:"))
num3= int (input("Enter third number:"))
avg= (num1+num2+num3)/3
print("Average of the three numbers is ",avg)

#Find square and cube of a number

num= int(input("Enter number:"))
sq= num*num
cube= num*num*num
print("Square is ",sq ,"and Cube is ", cube)

#Swap two numbers without third variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a = a + b
b = a - b
a = a - b
print("After swapping:")
print("a =", a)
print("b =", b)

#Student report program

name= input("Enter student's name:")
age= int (input("Enter student's age:"))
#entering and storing marks of five subjects in variables
english= float(input("Enter marks in english:"))
hindi= float(input("Enter marks in hindi:"))
maths= float(input("Enter marks in maths:"))
science= float(input("Enter marks in science:"))
social_science = float(input("Enter marks in social science:"))
#Calculating total marks
total= english +hindi + maths + science + social_science
#Calculate percentage
percent= ((total)/500)*100
# Display report
print("STUDENT REPORT\n")
print("Name:", name)
print("Age:", age)
print("Hindi:", hindi)
print("Maths:", maths)
print("Science:", science)
print("English:", english)
print("Social Science:", social_science)
print("Total Marks:", total)
print("Percentage:", percent, "%")










          

#ASSIGNMENT 1
 
# #Area of Rectangle
length=int(input("Enter length of rectangle: "))
breadth=int(input("Enter breadth of rectangle: "))
area=length*breadth
print("Area of Rectangle is: ",area)

#Simple interest
p=int(input("Enter Principal amount: "))
r=int(input("Enter Rate of interest per year: "))
t=int(input("Enter Time(in years): "))
si=(p*r*t)/100
print("Simple interest calculated is: ",si)

#Temperature converter Celsius to Fahrenheit
C=int(input("Enter temperature in Celsius: "))
F=(C*9/5)+32
print("Equivalent Temperature in Fahrenheit is: ",F)

#Average calculator
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
avg=(num1+num2+num3)/3
print("Average of three numbers is: ",avg)

#square and cube of a number
n=int(input("Enter a number: "))
square=n**2
cube=n**3
print("Square of",n,"is",square)
print("Cube of",n,"is",cube)

#Swap two numbers without third variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)

#Student Report Program

#Taking name as user input
name=input("Enter your Name: ")

#Taking marks of 5 subjects as user input
marks1=int(input("Enter marks for subject 1: "))
marks2=int(input("Enter marks for subject 2: "))
marks3=int(input("Enter marks for subject 3: "))
marks4=int(input("Enter marks for subject 4: "))
marks5=int(input("Enter marks for subject 5: "))

#Calculating total marks
total=marks1+marks2+marks3+marks4+marks5

#Calculating percentage
percentage=(total/500)*100

print("Percentage for student",name,"is",percentage)
print("Total marks obtained by",name,"is",total)

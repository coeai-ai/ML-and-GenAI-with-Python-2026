# 1.Area of rectangle
length=float(input("Enter length:"))
breadth=float(input("Enter breadth:"))
area=length * breadth
print("Rectangle area:", area)


# 2.simple interest
p=float(input("Enter principal:"))
r=float(input("Enter Rate:"))
t=float(input("Enter time:"))
si=(p * r * t)/100
print("Simple Interest is:",si)


#3.Convert temperature from celsius to fahrenheit
celsius=float(input("Enter temperature in celsius:"))
fahrenheit=(celsius * 9/5)+32
print("Temperature in fahrenheit",fahrenheit)


# 4.Average
a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))
average=(a+b+c)/3
print("Average:",average)


# 5.Square and cube of a number
a=int(input("Enter the number:"))
Square=a ** 2
Cube=a ** 3
print("Square:",Square)
print("Cube:",Cube)


#6. Swap the two numbers
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
a,b=b,a
print(" a and b are :",a,b)


#7.Student Report Program:
Name=input("Enter Student name:")
roll_no =input("Enter roll number:")
#Marks of the subjects
Maths=float(input("Enter Marks:"))
Physics=float(input("Enter Marks:"))
Chemistry=float(input("Enter Marks:"))
English=float(input("Enter Marks:"))
PHE =float(input("Enter Marks:"))
#Total
Total = Maths+Physics+Chemistry+English+PHE
#Percentage
percentage=Total/5
print(" Student Report ")
print("Name:",Name)
print("Roll Number:",roll_no)
print("Total Marks:",Total)
print("Percentage:",percentage,"%")



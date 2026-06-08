#1.Find area of rectangle
Length = int(input("enter the lenth of rectangle: "))
breadth = int(input("enter the lenth of rectangle: "))
print(f'area of rectangle is: {Length * breadth}')

#2.Find simple interest. 
p= int(input("enter the principle amount: "))
r= int(input("enter the rate: "))
t= int(input("enter the time period: "))
print(f'the simple interest is: {(p*r*t)/100}')

#3.Convert temperature from Celsius to Fahrenheit. 
c=int(input("enter the celcius: "))
f= (c*1.8)+32
print(f'the temp in farenite: {(f)}')

#4.Calculate average of 3 numbers. 
First= int(input("enter the first no: "))
Second= int(input("enter the second no: "))
Third= int(input("enter the third no: "))
average = (First+Second+Third)/3
print(average)

#5.Find square and cube of a number. 
num= int(input("enter a no: "))
print(f'the square of no is: {num**2} and cube is: {num**3}')

#6.Swap two numbers without third variable.
a=int(input("enter a no: "))
b=int(input("enter a no: "))
a=a+b
b=a-b
a=a-b
print(f'after swapping a is : {a}  and b is : {b}')

#7.Create a Student Report Program that take student details using input(), Store marks in variables, Calculate total and percentage , Use comments, Use proper indentation
name = input("Enter name:")
roll_no = int(input("Enter roll number:"))
# Subjects 
Maths = int(input("Enter marks of maths:"))
English = int(input("Enter marks of english:"))
Science = int(input("Enter marks of science:"))
Total = Maths + English + Science
Percentage = (Total/300)*100
print("/n___STUDENT REPORT_")
print("Name:",name)
print("Roll number :",roll_no)
print("Maths marks:",Maths)
print("English marks:",English)
print("Science marks:",Science)
print("Total marks:",Total)
print("Percentage:",Percentage)
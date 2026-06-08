#code 1
length=int(input("Enter the length of rectangle:"))
breadth=int(input("Enter the breadth of the rectangle:"))
Area=length*breadth
print(f"The area of the rectangle is{Area}")
#code 2
Principal=int(input("Enter the  principal amount : "))
Rate=int(input("Enter the rate in percentage : "))
Time=int(input("Enter the  time period : "))
SI=(Principal*Rate*Time)/100
print(f"The simple interest is {SI}")
#code 3
Temp_cel=float(input("Enter  the temp in celsius:"))
temp_fr=(Temp_cel*1.8)+32
print(f"the temperature in fahrenheit is {temp_fr}F")
#code 4
num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))
num3=int(input("Enter third number : "))
av_nums=(num1+num2+num3)/3
print(f"the average of the numbers is {av_nums}")
#code 5
num=int(input("Enter the number : "))
sq=num**2
cube=num**3
print(f"Cube is : {cube}","\n",f"Square is : {sq}")
#code 6
num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))
num1,num2=num2,num1
print(num1,num2)
#code 7
Name=input("Enter your name : ")
Roll_no=int(input("Enter your roll no. : "))
Class=int(input("Enter your class : "))
Marks_subj1=int(input("Enter your marks for first subject : "))
Marks_subj2=int(input("Enter your marks for second subject : "))
Marks_subj3=int(input("Enter your marks for third subject : "))
total=Marks_subj1+Marks_subj2+Marks_subj3
print(f"total marks obtained are {total}")
total_marks=int(input("Enter the total marks of all 3 subjects : "))
per=(total/total_marks)*100
print(f"Percentage : {per}")
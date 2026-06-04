# Ques1. Find area of a rectangle.
length=5
breadth=3
area=length*breadth
print("Area of a rectangle with length 5 and breadth 3 is :",area)

#Ques2. Find simple interest.
Principle=5000
rate=2
time=1
simpleInterest=(Principle*rate*time)/100
print("The simple interest is ",simpleInterest)

#Ques3. Calculate temperature from Celsius to Fahrenheit.
celsius=35
fahrenheit=(celsius*(9/5))+32
print("35 degree celsius in Fahrenheit is : ",fahrenheit)

#Ques4. Calculate average of 3 numbers.
num1=15
num2=85
num3=90
average=(num1+num2+num3)/3
print("Average of 15,85,90 is : ",average)

#Ques5. Find square and cube of a number.
number=5
square=number*number
cube=square*number
print("Square of 5 is : ",square," and cube of 5 is : ",cube)

#Ques6. Swap two numbers without third  variable
a=9
b=5
a,b=b,a
print(" a = ",a)
print(" b = ",b)

# Create a Student Report Program that take student details using input(), Store marks in variables, Calculate total and percentage 
name=input("Enter your name : ")
roll_number=input("Enter your roll number : ")
english=int(input("Enter your english marks : "))
hindi=int(input("Enter your hindi marks : "))
maths=int(input("Enter your maths marks : "))
science=int(input("Enter your science marks : "))
total=(english+hindi+maths+science)
percent=total/4
print("Your total marks are ",total)
print("Your percentage is : ",percent)

"""
Below is the result I got after running the program

Area of a rectangle with length 5 and breadth 3 is : 15
The simple interest is  100.0
35 degree celsius in Fahrenheit is :  95.0
Average of 15,85,90 is :  63.333333333333336
Square of 5 is :  25  and cube of 5 is :  125
 a =  5
 b =  9
Enter your name : radha
Enter your roll number : 161
Enter your english marks : 95
Enter your hindi marks : 98
Enter your maths marks : 86
Enter your science marks : 92
Your total marks are  371
Your percentage is :  92.75
"""
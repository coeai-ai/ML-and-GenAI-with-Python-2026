#ASSINGMENT-2

#Find sum of 10 natural number
sum=0
for i in range(1,11,1):
    sum+=i
print("Sum of 10 natural number is ",sum)

#Find factorial of a number
f=1
n=int(input("Enter a number:"))
for i in range(1,n+1):
    f*=i
print("Factorial is:",f)

#Print Fibonacci Series
a=0
b=1
n= int(input("Enter how many fibonacci numbers you want:"))
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    
# Find largest among 3 numbers
num1 = int (input("Enter first number:"))
num2 = int (input("Enter second number:"))
num3 = int(input("Enter third number:"))
if num1>num2:
    if num1>num3:
        print("Largest among the 3 numbers is :", num1)
elif num2>num1:
    if num2>num3:
        print("Largest among the 3 numbers is :", num2)
else:
    print("Largest among the 3 numbers is :", num3)

#Create Student Result system

while True:
    name= input("Enter Student's name:")
    age = int (input("Enter student's age:"))
    Roll_no= int(input("Enter roll no :"))
    science= float(input("Enter marks in science:"))
    maths= float(input("Enter marks in maths:"))
    english= float(input("Enter marks in english:"))
    percentage= ((science+ maths+ english)/300)*100
    print("Percentage:",percentage)
    if percentage > 95:
        print("Grade:O")
    elif percentage > 85:
        print("Grade:A")
    elif percentage > 75:
        print("Grade:B")
    elif percentage > 65:
        print("Grade:C")
    elif percentage > 45:
        print("Grade:D")
    else:
        print("Fail")
    o= int(input("Do you want to enter information of more students (enter for yes-1 and for no-0):"))
    if o==0:
        break
    
    

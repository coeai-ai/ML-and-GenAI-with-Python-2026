# Q1.first sum of 10 natural numbers
sum=0
for i in range(1,11):
       sum+=i
print("the sum of first 10 natural numbers is:",sum)

#Q2.factorial
num=int(input("enter a number:"))
factorial=1
for i in range(1,num+1):
    factorial *= i
print("the factorial is:",factorial)

#Q3.fibonacci series
num=int(input("enter the number of terms:"))
a=0
b=1
for i in range(num):
    print(a,end=" ")
    a,b=b,a+b

#Q4.to find the largest number
#taking 3 numbers from the user
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
num3=int(input("enter third number:"))
#checking for greatest using conditioms
if num1>=num2 and num1>=num3:
    print(num1,"is greatest.")
elif num2>=num1 and num2>=num3:
    print(num2,"is greatest.")
elif num3>=num2 and num3>=num1:
    print(num3,"is greatest.")
else:
    print("all are equal.")

#Q5.student result system
#taking details of student
name=input("enter your name:")
en_roll=input("enter your enrollment number:")
n=int(input("enter the number of subjects:"))
total=0
#finding marks of students
for i in range(1,n+1):
    marks=float(input("enter your marks for subject:"))
    total+=marks
#calculating percentage
percentage=(total/n)
print("name:", name)
print("enrollment no.:",en_roll)
print("your total marks is:", total)
print("your percentage is:",percentage)
#determing the grade and printing the grade
if percentage>=93 :
    print("your grade is: A+")
elif npercentage>=85:
    print("your grade is: A")
elif percentage>=77:
    print("your grade is: B+")
elif percentage>=69:
    print("your grade is: B")
elif percentage>=61:
    print("your grade is: C+")
elif percentage>=53:
    print("your grade is: C")
elif percentage>=45:
    print("your grade is: D")
else:
    print("Fail")
    
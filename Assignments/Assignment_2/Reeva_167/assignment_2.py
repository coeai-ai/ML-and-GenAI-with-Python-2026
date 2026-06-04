#1. Find sum of first 10 natural numbers
n=10
sum=n*(n+1)/2
print("Sum:\n",sum)

#2. Find the factorial of a number
num=int(input("Enter a number: "))
factorial=1
for i in range(1, num + 1):
    factorial *= i
print("Factorial:\n",factorial)

#3. Print Fibonacci Series
a=0
b=1
print(a,b,end=" ")
for i in range(10):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
print()

#4. Find largest among 3 numbers.
num1=float(input("Enter the first number: \n"))
num2=float(input("Enter the second number: \n"))
num3=float(input("Enter the third number: \n"))
if num1>num2 and num1>num3:
    print("The largest number is:",num1)
elif num2>num1 and num2>num3:
    print("The largest number is:",num2)
else:
    print("The largest number is:",num3)

#5. Create Student Result System
name=input("Enter the student's name: ")
roll_num=int(input("Enter roll number: "))
marks1=float(input("Enter marks for subject 1: \n"))
marks2=float(input("Enter marks for subject 2: \n"))
marks3=float(input("Enter marks for subject 3: \n"))
total=marks1+marks2+marks3
percentage=(total/300)*100
if percentage>=90:
    grade="A"
elif percentage>=80:
    grade="B"
elif percentage>=70:
    grade="C"
elif percentage>=60:
    grade="D"
else:
    grade="F"
print("Student Name:",name)
print("Roll Number:",roll_num)
print("Total Marks:",total)
print("Percentage:",percentage)
print("Grade:",grade)

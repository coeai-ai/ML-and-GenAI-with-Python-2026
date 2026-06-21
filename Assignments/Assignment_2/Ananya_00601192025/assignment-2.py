#Find sum of first 10 natural numbers.
sum=0
for i in range(1,11) :
    sum+=i
print("sum of first 10 natural numbers is ",sum)


#Find factorial of a number.
num=int(input("Enter a number to find its factorial: "))
fact=1
for i in range(1,num+1) :
    fact=fact*i
print("Factorial of ",num," is ",fact)


#Print Fibonacci Series.
a=0
b=1
n=int(input("Enter the number of terms in Fibonacci series: "))
for i in range(n):
    print(a,end=' ')
    a,b=b,a+b
print("")


#Find largest among 3 numbers.
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
n3=int(input("Enter third number: "))
max=n1
if n2>max :
    max=n2
if n3>max :
    max=n3
print("Largest number is ",max)


#Create Student Result System
#	-	Input student details 
#	-	Input marks
#	-	Calculate percentage 
#	-	Display grade 
#	-	Use: 
#if-elif-else 
#loops 
#user input

name=input("Enter student name: ")
roll_no=int(input("Enter student roll number: "))
marks=int(input("Enter student marks: "))
percentage=(marks/100)*100
if percentage>=90 :
    grade='A'
elif percentage>=80 :
    grade='B'
elif percentage>=70 :
    grade='C'
elif percentage>=60 :
    grade='D'
else :
    grade='F'
print("Student Name: ",name)
print("Roll Number: ",roll_no)
print("Marks: ",marks)
print("Percentage: ",percentage)
print("Grade: ",grade)
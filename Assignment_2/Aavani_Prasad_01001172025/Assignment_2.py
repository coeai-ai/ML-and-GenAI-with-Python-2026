#Aavani Prasad
#Assignment 2

#1 Find sum of first ten natural numbers
s=sum(range(1,11))
print(f"Sum of first ten natural numbers is: {s}")

#2 Find factorial of a number
n=int(input("Enter number:"))
factorial=1
if n<0:
    print("Factorial does not exist for negative numbers")
elif n==0:
    print("Factorial of 0 is 1.")
else:
    for i in range(1,n+1):
        factorial=factorial*i
    print(f"Factorial of {n} is {factorial}")

#3 Print Fibonacci Series
a,b=0,1
n=int(input("Enter number greater than 1 for series:"))
series=[]
for i in range(1,n+1):
    series.append(a)
    a,b=b,a+b
print(series)

#4 Find largest among three numbers
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
c=float(input("Enter third number:"))
if a>b and a>c:
    largest=a
elif b>a and b>c:
    largest=b
else:
    largest=c
print("Largest number:",largest)

#5 Student result system

#Taking student details
name=input("Enter name:")
age=input("Enter age:")
grade=input("Enter class:")
#Input Marks
phy_marks=float(input("Enter physics marks:"))
math_marks=float(input("Enter mathematics marks:"))
bio_marks=float(input("Enter biology marks:"))
chem_marks=float(input("Enter chemistry marks:"))
eng_marks=float(input("Enter english marks:"))
#Calculate percentage
total=phy_marks+math_marks+bio_marks+eng_marks+chem_marks
p=total/5
print("Percentage=",p)
#Display grade
if p>=90:
    g="A+"
elif p>=80 and p<90:
    g="A"
elif p>=60 and p<80:
    g="B+"
elif p>=50 and p<60:
    g="B"
elif p>=40 and p<50:
    g="C"
elif p>=33 and p<40:
    g="D"
else:
    g="F"
print("Grade=",g)




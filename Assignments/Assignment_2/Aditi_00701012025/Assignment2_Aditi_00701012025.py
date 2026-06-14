#sum of first 10 natural numbers
sum=0
for i in range(1,11):
    sum+=i
print("Sum of first 10 natural numbers is:",sum)

#factorial of a number
num=int(input("Enter a number:"))
fact=1
for i in range(1,num+1):
    fact*=i
print("Factorial of given number is:",fact)

#Fibonacci series
num1=int(input("Enter the numbers of terms in Fibonacci series:"))
f1=0
f2=1
print(f1)
print(f2)
for i in range(3,num1+1):
    f3=f1+f2
    print(f3)
    f1=f2
    f2=f3

#largest among 3 numbers
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
largest=num1
if num2>num1:
    largest=num2
    if num3>num2:
        largest=num3
print("Largest number among 3 numbers is:",largest)

#student result system
name=input("Enter student's name:")
roll=int(input("Enter student's roll number:"))
mark1=float(input("Enter subject 1 marks:"))
mark2=float(input("Enter subject 2 marks:"))
mark3=float(input("Enter subject 3 marks:"))
total=mark1+mark2+mark3
perc=(total/300)*100
print("Percentage is:",perc)
if perc>=90:
    print("A grade")
elif perc>=80:
    print("B grade")
elif perc>=70:
    print("C grade")
elif perc>=60:
    print("D grade")
else:
    print("FAIL")




    


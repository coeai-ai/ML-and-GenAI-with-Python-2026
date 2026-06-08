#1.Find sum of first 10 natural numbers.
sum=0
for i in range(1,11):
    sum+=i
print(f'sum of first 10 natural no is : {sum}')

#2.Find factorial of a number.
n= int(input("Enter a no: "))
factorial =1 
for i in range(1,n+1):
    factorial*=i
print(f'factorial of n is : {factorial}')

# print Fibonacci series.
n = 10
a,b = 0,1
print("Fibonacci series:")
for i in range(n):
    print(a,end=' ')
    a=b
    b=a+b

#Find largest among 3 numbers.
num1 = 8
num2 = 70
num3 = 2
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print("The largest number among",num1,",",num2,"and",num3,"is:",largest)

#create student result system.
name = input("Enter student name:")
age = int(input("Enter student age:"))
marks = int(input("Enter marks obtained:"))
if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = 'E'
percentage = (marks/100)*100
print("student name:",name)
print("student age:",age)
print("marks obtained:",marks)
print("percentage:",percentage)
print("grade:",grade)
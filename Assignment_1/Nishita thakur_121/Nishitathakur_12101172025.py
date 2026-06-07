# Find the sum of first 10 natural numbers.
n = 10
sum = n*(n+1)/2
print("The sum of first 10 natural numbers is:",sum)
 
#Find factorial of a number.
num = 5
factorial = 1
for i in range(1,num+1):
    factorial = factorial * i
    print("The factorial of",num,"is:",factorial)

# print Fibonacci series.
n = 10
a,b = 0,1
print("Fibonacci series:")
for i in range(n):
    print(a,end=' ')
    a,b = b,a+b

#Find largest among 3 numbers.
num1 = 10
num2 = 20
num3 = 15
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
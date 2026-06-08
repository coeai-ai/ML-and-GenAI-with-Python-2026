#ASSIGNMENT 2

#Q1. Find sum of first 10 natural numbers

sum = 0
for i in range(1,11):
        sum = sum + i        
print("the sum of first 10 natural numbers is:", sum)


#Q2. Find factorial of a number

n = int(input("enter the number you want factorial of:"))
fact = 1
for i in range(1, n+1):
        fact = fact*i

print("the factorial of", n ,"is", fact)


#Q3. Print fibonnaci series

n = int(input("enter the number of terms:"))
a = 0
b = 1
for i in range(n):
        print(a, end=" ")
        c = a + b 
        a = b
        b = c


#Q4. Find largest among three numbers

a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
c = int(input("enter the third number:"))

if a>b and a>c:
        print("the largest number is:", a)
elif b>c and b>a:
        print("the largest number is:", b)
else:
        print("the largest number is:", c)


#Q5.  Create student result system

name = input("enter the name:")
roll_no = int(input("enter the roll number:"))
marks = int(input("enter the total marks out of 500:"))
percentage = (marks/500) * 100

print("NAME:", name)
print("ROLL NO.:", roll_no)
print("MARKS:", marks)
print("PERCENTAGE OBTAINED:",percentage)

if percentage >= 80 and percentage <= 100:
    print("THE GRADE OBTAINED IS 'A'")
elif percentage >= 70 and percentage < 80:
    print("THE GRADE OBTAINED IS 'B'")
elif percentage >= 60 and percentage < 70:
    print("THE GRADE OBTAINED IS 'C'")
elif percentage >= 40 and percentage < 60:
    print("THE GRADE OBTAINED IS 'D'")
else:
    print("THE GRADE OBTAINED IS 'E'")
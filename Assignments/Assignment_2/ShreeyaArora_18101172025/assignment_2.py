#1
summ = 0
for i in range(1,11):
    summ += i
print(f"Sum of first 10 natural numbers is: {summ}")

#2
n = int(input("Enter a number: "))
if n < 0:
    print("Factorial does not exist for negative numbers")
else:
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(f"Factorial of {n} is : {fact}")

#3
n = int(input("Enter number of fibonacci terms: "))
a=0
b=1
for i in range(n):
    print(a, end=" ")
    c=b
    b=a+b
    a=c
print()

#4
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
n3 = int(input("Enter third number : "))

if n1 >= n2 and n1 >= n3:
    print(f"{n1} is the greatest")
elif n2 >= n1 and n2 >= n3:
    print(f"{n2} is the greatest")
else:
    print(f"{n3} is the greatest")

#5
# Student Result System
print("##### Student Details #####")
print()
name = input("Enter your Name: ")
enrol_no = input("Enter your enrolment Number: ")
print()

print("##### Marks #####")
num1 = float(input("Enter your Maths marks: "))
num2 = float(input("Enter your Science marks: "))
num3 = float(input("Enter your English marks: "))
num4 = float(input("Enter your Hindi marks: "))
num5 = float(input("Enter your Social Studies marks: "))
print()

total = (num1+num2+num3+num4+num5)
percentage = total/5

print("|||||||||  STUDENT REPORT CARD |||||||||")

print("\n##### Student Details #####")
print(f"Student Name: {name}")
print(f"Enrolment Number : {enrol_no}")
print()
print("\n##### Marks Obtained #####")
print(f"Marks obtained in Maths: {num1}")
print(f"Marks obtained in Science: {num2}")
print(f"Marks obtained in English: {num3}")
print(f"Marks obtained in Hindi: {num4}")
print(f"Marks obtained in Social Studies: {num5}")

print("\n##### Result #####")

print(f"Total Marks Obtained: {total}")
print(f"Percentage Received: {percentage} %") 
print("Grade Obtained is: ", end = "")
if percentage >= 90:
    print("A+")
elif percentage >= 80:
    print("A")
elif percentage >= 70:
    print("B+")
elif percentage >= 60:
    print("B")
elif percentage >= 50:
    print("C+")
elif percentage >= 40:
    print("C")
else:
    print("F")


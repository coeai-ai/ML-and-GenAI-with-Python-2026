#1

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))

print(f"Area of Rectangle with length {l} and breadth {b} is: {l*b}")

#2
p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter Time in years: "))

si = (p * r * t) / 100

print(f"Simple Interest on {p} for {t} years is: {si}")

#3
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print(f"Temperature in Fahrenheit is: {f}")

#4
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

avg = (num1+num2+num3)/3

print(f"Average of {num1},{num2},{num3} is: {avg}")

#5

num = int(input("Enter a number: "))

square = num ** 2
cube = num ** 3
print(f"Square of {num} is: {square}")
print(f"Cube of {num} is: {cube}")

#6
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

summ = num1+num2

num1 = summ-num1
num2 = summ-num2

print(f"First number after swapping is: {num1}")
print(f"Second number after swapping is: {num2}")

#7
# Entering student details by inputing them

name = input("Enter your full Name: ")
enrol_no = input("Enter your Enrolment Number: ")

# Entering marks for different subjects by inputing them

Maths = float(input("Enter your Maths Marks: "))
Science = float(input("Enter your Science Marks: "))
SocialStudies = float(input("Enter your Social Studies Marks: "))
English = float(input("Enter your English Marks: "))
Hindi = float(input("Enter your Hindi Marks: "))


# Calculating total marks of subjects and percentage
summ = (Maths + Science + SocialStudies + English + Hindi)
percentage = summ/5

# Displaying student report
print()
print("###### STUDENT REPORT ######")
print()
print(f"Name of the Student is: {name}")
print(f"Enrolment Number of the Student is: {enrol_no}")
print(f"Total Marks obtained is: {summ}")
print(f"Percentage received is: {percentage:.2f} %")
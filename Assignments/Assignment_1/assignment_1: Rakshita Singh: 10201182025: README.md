#NAME = RAKSHITA SINGH
#ROLL NO = 10201182025
#COLLEGE NAME = IGDTUW


# Q1. Find the area of rectangle

length = int(input("enter the length of the rectangle: "))
base = int(input("enter the base of the rectangle: "))
area = length * base
print("the area of rectangle is:", area)


#Q2. Find the simple interest
amount = float(input("enter the principle amount: "))
rate = float(input("enter the rate of interest: "))
time = int(input("enter the year: "))
simple_interest = (amount * rate * time)/ 100
print("the simple interest is:", simple_interest)



#Q3. Convert temperature from celsius to fahrenheit
cel = int(input("enter the temperature in celsius:"))
fahrenheit = (cel * 9/5) + 32
print("the temperature in fahrenheit is:", fahrenheit)


#Q4. Calculate average of 3 numbers
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
c = int(input("enter the third number:"))
avg = (a + b + c) / 3
print("the average of three numbers is:", avg)


#Q5. Find sqaure and cube of a number
num = int(input("enter the number"))
sqaure = print("the sqaure of the number is:", num**2)
cube = print("the cube of the number is:", num**3)


#Q6. Swap two numbers without third variable
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
a, b = b, a
print("a =", a)
print("b =", b)


#Q7. Create a student report program that take student details using input(),
# store marks in variables, calculate total and percentage, use comments, use proper indentation.
name = input("enter the name of the student:")
roll_no = int(input("enter the roll number of the student:"))

sub_1 = int(input("enter the marks in subject 1:"))
sub_2 = int(input("enter the marks in subject 2:"))
sub_3 = int(input("enter the marks in subject 3: "))
total = sub_1 + sub_2 + sub_3
percentage = total/3

print("STUDENT REPORT")
print("NAME:", name)
print("ROLL NO.:", roll_no)
print("MARKS IN 1ST SUBJECT:", sub_1)
print("MARKS IN 2ND SUBJECT:", sub_2)
print("MARKS IN 3RD SUBJECT:", sub_3)
print("TOTAL MARKS:", total)
print("PERCENTAGE:", percentage)




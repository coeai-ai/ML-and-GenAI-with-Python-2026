#1. area of rectangle :
a=11
b=5
area = a*b
print("area of rectangle is ",area)
# 2.Finding out simple interest:
p = 10
r = 5
t = 2
s_int = (p*r*t)/100
print("simple interest is ",s_int)
# 3. Temp from celcius to fahrenheit:
temp = bool(input("enter the temp"))
ft = (temp * 9/5)+32
print("temperature in fahrenbeit would be ",ft)
# 4. average of three numbers
num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))
num3 = int(input("enter the third number"))
avg = (num1+num2+num3)/3
print("average of the three number will be",avg)
# 5. square & cube of a number
a = int(input("enter the number"))
b = int(input("enter the number"))
sq1 = a**2
sq2 = b**2
print("square of a",sq1)
print("square of b",sq2)
print("cube of a",a**3)
print("cube of b",b**3)
# 6.swap two numbers without third variable
a = int(input("enter the first number"))
b = int(input("enter the second number"))
a,b = b,a
print("after swapping")
print("a =",a)
print("b =",b)
# 7. Student report System
name = input("enter your name")
roll_no = int(input("enter the number"))
mark1 = float(input("Enter marks of subj 1"))
mark2 = float(input("Enter marks of subj 2"))
mark3 = float(input("Enter marks of subj 3"))
total = mark1+mark2+mark3
percentage = total/3
print("Name is",name)
print("Rollno. is",roll_no)
print("marks is",mark1, mark2, mark3)
print("Total is ",total)
print("Percentage", percentage,"%")





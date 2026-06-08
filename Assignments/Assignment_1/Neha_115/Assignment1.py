# 1.Find area of rectangle
length=int(input("enter the length:"))
width=int(input("enter the width:"))
area=length*width
print("area:",area)

# 2.Find simple interest.
print("formula=p*r*t/100")
p=float(input("enter principle:"))
r=float(input("enter rate:"))
t=float(input("enter time:"))
SI=p*r*t
print("SI:",SI)

# 3.Convert temperature from Celsius to Fahrenheit.
temp_C=float(input("enter temperature in celsius:"))
temp_F=temp_C*(9/5)+32
print("temperature in fahrenheit:",temp_F)

# 4.Calculate average of 3 numbers.
num1=float(input("enter first no.:"))
num2=float(input("enter second no.:"))
num3=float(input("enter third no.:"))
avg=(num1+num2+num3)/3
print("average of 3 numbers:",avg)

# 5.Find square and cube of a number
num=int(input("enter the number:"))
square=num**2
cube=num**3
print("cube of",num,":",cube)
print("square of",num,":",square)

# 6.Swap two numbers without third variable.
num1=int(input("enter first no.:"))
print("num1 before swapping:",num1)
num2=int(input("enter second no.:"))
print("num2 before swapping:",num2)
num1=num1+num2
num2=num1-num2
num1=num1-num2
print("num1 after swaping:",num1)
print("num2 after swapping:",num2)

# 7.Create a Student Report Program that take student details using input(), Store marks in variables, Calculate total and percentage , Use comments, Use proper indentation
# Taking student details as input
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Taking marks of 3 subjects
maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))

# Calculating total marks
total = maths + science + english

# Calculating percentage
percentage = (total / 300) * 100

# Displaying student report
print("\n----- STUDENT REPORT -----")
print("Name:", name)
print("Roll Number:", roll_no)
print("Maths Marks:", maths)
print("Science Marks:", science)
print("English Marks:", english)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
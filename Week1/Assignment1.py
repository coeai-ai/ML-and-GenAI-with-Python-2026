# QUESTION 1
length = int(input("ENTER LENGTH :>"))
width = int(input("ENTER WIDTH :>"))
area = length * width
print( "Area of the rectangle = " ,area ,"sq units")

#QUESTION 2
p = int(input("Principal amount = "))
r = int(input("Rate of interest(%) = "))
t = int(input("Time(in years) = "))
Simple_interest = (p*r*t)/100
print("simple interest = " ,Simple_interest)

#QUESTION 3
a = int(input(("Enter temperture (in degree celcius) : ")))
convert = (a*9)/5 + 32
print("Temperture in Fahrenheit = " ,convert)

# QUESTION 4
num1 = int(input(" number 1 = "))
num2 = int(input(" number 2 = "))
num3 = int(input(" number 3 = "))
average = (num1+num2+num3)/3
print("Average of the three numbers = " ,average)

#QUESTION 5
nums = int(input("Enter number :> "))
sq = nums**2
cube = nums**3
print("square = ", sq ,"\n", "cube = ", cube)

# QUESTION 6
a = int(input(" number 1 = "))
b = int(input(" number 2 = "))
a, b = b,a
print("number 1 =" ,a,"\n","number 2 = ",b)

# QUESTION 7 
 
# Taking student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Taking marks
mark1 = int(input("Enter marks of Subject 1: "))
mark2 = int(input("Enter marks of Subject 2: "))
mark3 = int(input("Enter marks of Subject 3: "))
mark4 = int(input("Enter marks of Subject 4: "))
mark5 = int(input("Enter marks of Subject 5: "))

# Calculating total marks
total = mark1 + mark2 + mark3 + mark4 + mark5

# Calculating percentage
percentage = total / 5

# Displaying report
print("\n----- STUDENT REPORT -----")
print("Name:", name)
print("Roll Number:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage, "%")

 
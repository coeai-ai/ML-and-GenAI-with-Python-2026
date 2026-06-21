#area of rectangle
length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))
area = length * breadth
print("The area of the rectangle is", area)

#simpl;e interest
principal = int(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = int(input("Enter the time in years: "))
simple_interest = (principal * rate * time) / 100
print("The simple interest is", simple_interest)

# temperature from celcius to fahrenheit
celcius = float(input("Enter the temperature in celcius: "))
fahrenheit = (celcius * 9/5) + 32
print("The temperature in fahrenheit is", fahrenheit)

# average of three numbers 
a = int(input("enter the number "))
b = int(input("enter the second number"))
c = int(input("enter the third number"))
average = (a+b+c)/3
print("the average of the three numbers is", average)

# square of a number
number = int(input("Enter a number "))
square = number ** 2
print("The square of the number is", square)    

# cube of a number
number = int(input("Enter a number "))
cube = number ** 3
print("The cube of the number is", cube)

# swap two numbers without third number
a = int(input("Enter the first number "))
b = int(input("Enter the second number "))
a = a + b
b = a - b       
a = a - b
print("After swapping, the first number is", a)
print("After swapping, the second number is", b)

# student report

# Taking student details as input
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Taking marks as input
maths = int(input("Enter Maths Marks"))
science = int(input("Enter Science Marks"))
english = int(input("Enter English Marks"))

# Calculating total marks
total = maths + science + english

# Calculating percentage
percentage = (total / 300) * 100

# the student report
print("Student Name ", name)
print("Roll Number  ", roll_no)
print("Maths Marks  ", maths)
print("Science Marks ", science)
print("English Marks ", english)
print("Total Marks  ", total)
print("Percentage   ", percentage, "%")






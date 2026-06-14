# Q1 to find area of a rectangle.
a = int(input("Enter the length:"))
b = int(input("Enter the breadth:"))
print("The area of the rectangle is: a*b =",a*b)


# Q2 to find simple interest
print("To find the simple interest")
P = int(input("Enter Principle:"))
R = int(input("Enter the Rate of interest:"))
T = int(input("Time:"))
print("Simple interest =",(P*R*T)/100,)


# Q3 Convert temperature fom celsius to fahrenheit
C = float(input("Enter the temperature in celsius:"))
print("Temperature in fahrenheit (F)= ((9/5)*C)+32",((9/5)*C)+32)


# Q4 calculate the average of three numbers
a = int(input("First number:"))
b = int(input("Second number:"))
c = int(input("Third number:"))
print("The Average of the no.s is: ",(a+b+c)/3)


# Q5 To find cube and sqaure of a number
x = int(input("Enter a number:"))
print("Sqaure of x is:",x**2)
print("Cube of x is:",x**3)


# Q6 Swap two variable without using a third variable
x = int(input("Enter value for x:"))
y = int(input("Enter value for y:"))
x, y = y, x
print("After swapping x =",x,",y =",y)


# Q7 student report
# taking input for students details
name = input("Enter your name:")
rollno = int(input("Enter your roll no.:"))
# takinng input for marks
phy_marks = int(input("Enter physics marks:"))
chem_marks = int(input("Enter chemistry marks:"))
maths_marks = int(input("Enter maths marks:"))
# to find the total marks
total = phy_marks + chem_marks + maths_marks
print("Total marks:",total)
# to find the percentage
percentage = (total/300)*100
print("Percentage is:",percentage)

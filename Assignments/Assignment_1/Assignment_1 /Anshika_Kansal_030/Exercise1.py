# question 1
def finding_Area(l,b):
    return (l*b)

print("Area of rectangle is :",finding_Area(3,4))
print("Area of rectangle is :",finding_Area(9,3))

# question 2
def Simple_interest(p,r,t):
    return p*r*t/100

print("Simple Interest is :",Simple_interest(3,4,3))
print("Simple Interest is :",Simple_interest(9,4,3))

#question 3

def temp_converter(temp):
    return (temp*9/5)+32

print("celsius temp converted in fahrenheit is :",temp_converter(32))

#question 4
def average(num1,num2,num3):
    return (num1+num2+num3)/3

print("Average is :",average(3,4,3))

#question 5
def square_and_cube(num):
    cube= num*num*num
    square= num**2
    return cube,square
print("Square and Cube is :",square_and_cube(3))

#question 6
a = 10
b = 20

a = a + b
b = a - b
a = a - b

print (a,b)

#question 7
# taking input from the user -- marks and name
name=str(input("enter your name:"))
subject1 = int(input("enter your marks:"))
subject2 = int(input("enter your marks:"))
subject3 = int(input("enter your marks:"))
subject4 = int(input("enter your marks:"))
subject5 = int(input("enter your marks:"))
subject6 = int(input("enter your marks:"))

# FiNDING TOTAL MARKS AND PERCENTAGE
total_marks_obtained = (subject1+subject2+subject3+subject4+subject5+subject6)
percentage = (total_marks_obtained/600)*100

print("total marks obtained are :",total_marks_obtained)
print("percentage is :",percentage)


#Assignment 01

#Find area of rectangle.
def question1():
    length=int(input("Enter length of rectange: "))
    width=int(input("Enter width of rectange: "))
    Area=length*width
    print("Area of rectangle is: ",Area," units")

#Find simple interest.
def question2():
    p=int(input("Enter principle value: "))
    r=int(input("Enter rate: "))
    t=int(input("Enter time(in years): "))
    si=(p*r*t)/100
    print("Simple Interest: ",si)

#Convert temperature from Celsius to Fahrenheit.
def question3():
    temp_C=float(input("Enter temp in Celsius: "))
    temp_F=(temp_C*9/5)+32
    print("Temp in Fahrenheit: ",temp_F)

#Calculate average of 3 numbers.
def question4():
    x=float(input("Enter first no.: "))
    y=float(input("Enter second no.: "))
    z=float(input("Enter thirdt no.: "))
    avg=(x+y+z)/3
    print("Average of no.s is: ",avg)

#Find square and cube of a number.
def question5():
    x=int(input("Enter a no.: "))
    sqr=x**2
    cube=x**3
    print("Square of no. is: ",sqr)
    print("Cube of no. is: ",cube)
    
#Swap two numbers without third variable.
def question6():
    x=int(input("Enter first no.: "))
    y=int(input("Enter second no.: "))
    print("x(before swap):",x)
    print("y(before swap):",y)
    x,y=y,x
    print("x(after swap):",x)
    print("y(after swap):",y)

#Create a Student Report Program that take student details using input), Store marks in variables, Calculate total and percentage, Use comments,
#Use proper indentation
def question7():
    marks={}
    print("Enter your marks of 5 subj (out of 100): ")
    total_m=0
    for i in range(0,5):
        marks[i]=int(input("marks: "))
        total_m=total_m+marks[i]
    percentage=(total_m/500)*100
    print("Total marks: ",total_m)
    print("Percentage: ",float(percentage),"%")

question1()
question2()
question3()
question4()
question5()
question6()
question7()

l = int(input("Enter the length:"))
b = int(input("Enter the breadth:"))
area = l*b
print("Area:",area)


principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time period (in yrs): "))
simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest
print("Simple Interest:",simple_interest)
print("Total amount payable:",total_amount)


c= int(input("Enter the temperature in celcius:"))
f= (c*9/5)+32
print("Temperature in fahrenheit:",f)


a=int(input("Enter the val of a:"))
b=int(input("Enter the val of b:"))
c=int(input("Enter the val of c:"))
avg= (a+b+c)/3
print("Averege:",avg)

n=int(input("Enter the value of n:"))
sqr = n**2
cube = n**3
print("Square:",sqr)
print("Cube:",cube)

a=int(input("Enter a:"))
b=int(input("Enter b:"))
a=a+b
b=a-b
a=a-b
print("After swapping:",a)
print("After swapping:",b)

name = input("Enter the name:")
age = int(input("Enter the age:"))
maths = int(input("Enter the marks in maths out of 100:"))    #marks in maths
phy = int(input("Enter the marks in physics out of:"))      #marks in physics
chem = int(input("Enter the marks in chemistry out of:"))     #marks in chemistry
total_marks = maths + phy + chem        #total marks in PCM
print("Total Marks:",total_marks)
percent = (total_marks/300)*100         #percentage in PCM
print("Percentage:",percent)



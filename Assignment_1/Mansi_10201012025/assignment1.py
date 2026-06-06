# 1 area of rectangle
l=float(input("Enter the length "))
b=float(input("Enter the breadth "))
area=l*b
print("The area of rectangel is ",area)

# 2. simple interest

p=float(input("Enter the principal amount "))
r=float(input("Enter the rate "))
t=float(input("Enter the time "))
si=p*r*t/100
print("Simple interest is ", si)


#3.convert temperature from clesius to fahrenheit

c=float(input("Enter the temperature in celsius "))
f=(9/5) * c + 32
print("temperature in fahrenheit is ",f)

#4 average of 3 numbers 
a=float(input("Enter the first number "))
b=float(input("Enter the second number "))
c=float(input("Enter the third number ")) 
average =a+b+c/3
print("the average of the numbers is",average)

# 5 find the square and cube of a number 

n=float(input("Enter the number "))
square=n**2
cube = n ** 3
print("Square =", square)
print("Cube =", cube)

# 6. Swap two numbers without third variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a=a+b
b=a-b
a=a-b
print("After swapping:")
print("a =", a)
print("b =", b)

#7  Student Report Program

name=input("Enter student name ")
roll_no=input("Enter student roll number ")
 
m1=float(input("Enter first subject marks "))
m2=float(input("Enter second subject marks "))
m3=float(input("Enter third subject marks "))

total=m1+m2+m3
percentage=total/3

print("Name of the stuent ",name)
print("Rollnumber of the stuent ",roll_no)
print("Total marks obtained by student",total)
print("Total percentage of the stuent",percentage)



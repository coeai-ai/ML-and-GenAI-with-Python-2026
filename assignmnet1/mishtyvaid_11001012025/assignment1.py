# 1 area of rectangle
length=float(input("Enter the length "))
breadth=float(input("Enter the breadth "))
area=length*breadth
print("The area of rectangle is : ",area)


# 2. simple interest
principle=float(input("Enter the principal amount "))
rate=float(input("Enter the rate "))
time=float(input("Enter the time "))
simple_interest=principle*rate*time/100
print("Simple interest is : ", simple_interest)



#3.convert temperature from clesius to fahrenheit
celsius=float(input("Enter the temperature in celsius "))
fahrenheit=(9/5) * celsius + 32
print("temperature in fahrenheit is : ",fahrenheit)


#4 average of 3 numbers 
num1=float(input("Enter the first number "))
num2=float(input("Enter the second number "))
num3=float(input("Enter the third number ")) 
average =(num1+num2+num3)/3
print("the average of the numbers is : ",average)


# 5 find the square and cube of a number 
num=float(input("Enter the number "))
square=num**2
cube = num ** 3
print("Square =", square)
print("Cube =", cube)


# 6. Swap two numbers without third variable
n1= int(input("Enter first number: "))
n2= int(input("Enter second number: "))
n1=n1+n2
n2=n1-n2
n1=n1-n2
print("After swapping:")
print("n1 =", n1)
print("n2 =", n2)


#7  Student Report Program
name=input("Enter student name ")
roll_no=input("Enter student roll number ")
s1=float(input("Enter first subject marks "))
s2=float(input("Enter second subject marks "))
s3=float(input("Enter third subject marks "))
percentage=(s1+s2+s3)/3
print("Name of the student ",name)
print("Roll number of the student ",roll_no)
print("Total marks obtained by the student ",s1+s2+s3)
print("Total percentage of the student ",percentage)
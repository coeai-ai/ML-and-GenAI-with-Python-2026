##question 1 
a= int(input("enter the length of the rectangle:"))
b= int(input("enter the breadth of the rectangle:"))
area = a * b
print("the area of the rectangle is:", area)


##question 2
a = int(input("enter the principel amount:"))
b = int(input("enter the rate of interest:"))
c = int(input("enter the time:"))
simple_interest = (a * b * c) / 100
print("the simple interest is:", simple_interest)


##question 3
a =int(input("enter the temperature in celsius:"))
fahrenheit = (a * 9/5) + 32
print("the temperature in fahrenheit is:", fahrenheit)  


##question 4
a =int(input("enter the first number:"))
b =int(input("enter the second number:"))
c= int(input("enter the third number:"))    
z = a + b+c
print("the average of the three numbers is:", z/3)


##question 5
a = int(input("enter the no."))
c= a**2
print("the square of the number is:", c)    
d= a**3
print("the cube of the number is:", d)      


##question 6
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
a,b = b,a
print("the value of a after swapping is:", a)
print("the value of b after swapping is:", b)


##question 7
a = int(input("enter the marks obtained:")) ##marks obtained
b = int(input("enter the maximum marks:")) ##maximum marks
c = (a/b) * 100
print("the percentage of the student is:", c)

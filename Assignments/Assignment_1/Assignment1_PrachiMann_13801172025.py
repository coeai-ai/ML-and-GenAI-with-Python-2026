#Area of rectangle

l = int(input("Enter length of rectangle : "))
b = int(input("Enter breadth of recangle : "))

area = l * b

print("The area of rectangle is : ", area)


#Simple interest

p = int(input("Enter principal or initial amount of money : "))
r = int(input("Enter rate of interest per year : "))
t = int(input("Enter time in years : "))

si = (p * r * t) / 100

print("The simple interest will be : ", si)


#Convert temperature from Celsius to Fahrenheit

temp_c = int(input("Enter temperature in celcius : "))

temp_f = ((9 * temp_c) / 5) + 32

print("The temperature in fahrenheit will be : ", temp_f)


#Calculate average of 3 numbers

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

average = (num1 + num2 + num3) / 3

print("The average of given numbers will be : ", average)


#Find square and cube of a number

num = int(input("Enter a number : "))

num_square = num ** 2
num_cube = num ** 3

print("The square of given number is : ", num_square)
print("The cube of given number is : ", num_cube)


#Swap two numbers without third variable

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print("Before swap : ")
print("a = ", a)
print("b = ", b)

a , b = b , a

print("After swap : ")
print("a = ", a)
print("b = ", b)


#Create a Student Report Program that take student details using input(), Store marks in variables, Calculate total and percentage , Use comments, Use proper indentation

maths = int(input("Enter marks obtained in maths subject (out of 100) : "))
science = int(input("Enter marks obtained in science subject (out of 100) : "))
english = int(input("Enter marks obtained in english subject (out of 100) : "))
hindi = int(input("Enter marks obtained in hindi subject (out of 100) : "))

#calculating total marks
total = maths + science + english + hindi

#calculating percentage
percentage = (total / 400) * 100

print("Total marks out of 400 is : ", total)
print("Percentage will be : ", percentage, "%")

# Find sum of first 10 natural numbers.

sum = 0

for i in range(1,11):
    sum += i

print("The sum of first 10 natural numbers is : ", sum)


# Find factorial of a number.

num = int(input("Enter a number : "))

fact = 1

for i in range(1, num+1):
    fact *= i

print("Factorial of ", num, " is ", fact)


# Print Fibonacci Series.

n = int(input("Enter how many numbers you want : "))

num1 = 0
num2 = 1

print(num1, num2, sep = " ", end = " ")

sum = 0

for i in range(n-2):
    sum = num1 + num2
    print(sum, end = " ")
    num1 = num2
    num2 = sum



# Find largest among 3 numbers.

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

largest = 0

if ((num1 > num2) & (num1 > num3)):
    largest = num1

elif ((num2 > num1) & (num2 > num3)):
    largest = num2

else:
    largest = num3

print("Largest number among given numbers is : ", largest)


# Create Student Result System

name = input("Enter your name : ")
maths = int(input("Enter marks obtained in maths subject (out of 100) : "))
science = int(input("Enter marks obtained in science subject (out of 100) : "))
english = int(input("Enter marks obtained in english subject (out of 100) : "))
hindi = int(input("Enter marks obtained in hindi subject (out of 100) : "))

total = maths + science + english + hindi

percentage = (total / 400) * 100

print("Percentage will be : ", percentage, "%")

grade = ''

if (percentage >= 90):
    grade = 'A'

elif (percentage < 90 & percentage >= 80):
    grade = 'B'

elif (percentage < 80 & percentage >= 70):
    grade = 'C'

elif (percentage < 70 & percentage >= 60):
    grade = 'D'

elif (percentage < 60 & percentage >= 50):
    grade = 'E'

else:
    grade = 'F'

print ("Grade of ", name, " is ", grade)
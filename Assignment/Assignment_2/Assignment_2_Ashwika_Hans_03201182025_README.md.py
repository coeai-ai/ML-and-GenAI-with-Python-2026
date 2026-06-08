#Student Name : Ashwika Hans
#Enrollment Number : 03201182025
#College Name : Indira Gandhi Delhi Technical University for Women

#Find sum of first 10 natural numbers
total = 0
for i in range(1, 11):
    total += i
print("The sum of first 10 natural numbers is : ", total)

#Find the factorial of a number
number = int(input("Enter a number to find its factorial : "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print("The factorial of the number is : ", factorial)

#Print fibonacci series 
n = int(input("Enter the number of terms in Fibonacci series : "))
a, b = 0, 1
print("Fibonacci series : ", end="")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()  # for new line

#Find the greatest of three numbers
num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))
num3 = float(input("Enter the third number : "))

if (num1 >= num2) and (num1 >= num3):
    greatest = num1
elif (num2 >= num1) and (num2 >= num3):
    greatest = num2
else:
    greatest = num3
print("The greatest of the three numbers is : ", greatest)

#Create Student Result System 
# Input student details
# Input marks 
#Calculate percentage
#Display grade
#Use: if-elif-else statements and loops

# Taking student details
name = input("Enter the student's name : ")
age = int(input("Enter the student's age : "))
grade = input("Enter the student's grade : ")

# Taking marks for three subjects
maths = int(input("Enter the marks for Maths : "))
science = int(input("Enter the marks for Science : "))
english = int(input("Enter the marks for English : "))
# Calculating total marks
total_marks = maths + science + english
# Calculating percentage
percentage = (total_marks / 300) * 100
# Displaying results
print("Student Name : ", name)
print("Age : ", age)
print("Grade : ", grade)
print("Total Marks : ", total_marks)
print("Percentage : ", percentage, "%")

# Determine grade based on percentage
if percentage >= 90:
    print("Grade : A")
elif percentage >= 80:
    print("Grade : B")
elif percentage >= 70:
    print("Grade : C")
elif percentage >= 60:
    print("Grade : D")
else:
    print("Grade : F")

#Find sum of first 10 natural numbers
sum = 0 
for i in range(1,11):
    sum += i
print(f"The sum of the first 10 natural numbers is: {sum}")   

#Find factorial of a number
fact = 1
num = int(input("Enter number for its factorial: "))
if num == 0:
   print("The factorial of 0 is 1. ")
elif num < 0:
   print("Factorial doesn't exist for negative nunbers.")
else:
   for i in range(1,num+1):
    fact = fact*i
   print(f"The factorial of {num} is : {fact}")


#Print Fibonacci Series
terms = int(input("How many terms of the Fibonacci series do you want? "))
n1, n2 = 0, 1  # First two terms
count = 0

if terms <= 0:
    print("Please enter a positive integer.")
elif terms == 1:
    print(f"Fibonacci series up to {terms} term: {n1}")
else:
    print("Fibonacci series:")
    while count < terms:
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    print()  

#Find largest among three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if (a >= b) and (a >= c):
    largest = a
elif (b >= a) and (b >= c):
    largest = b
else:
    largest = c
print(f"The largest number among {a}, {b}, and {c} is: {largest}")


#Student Result System
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

maths = float(input("Enter marks for Maths: "))
science = float(input("Enter marks for Science: "))
english = float(input("Enter marks for English: "))

total_marks = maths + science + english

percentage = (total_marks / 300) * 100

#Grading
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"

# Displaying the generated report card
print("\n" + "="*30)
print("        STUDENT RESULT        ")
print("="*30)
print(f"Name:        {name}")
print(f"Roll No:     {roll_no}")
print("-"*30)
print(f"Total Marks: {total_marks} ")
print(f"Percentage:  {percentage:.2f}%")
print(f"Grade:       {grade}")
print("="*30)

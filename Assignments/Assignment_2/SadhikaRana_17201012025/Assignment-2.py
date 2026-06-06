# 1. Find sum of first 10 natural numbers
sum = 0
for i in range(1,11):
    sum += i
print("Sum of first 10 natural numbers is: ", sum)

# 2. Find factorial of a number. 
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of the number is : ", factorial)

# 3. Print fibonacci series
n = int(input("Enter the number: "))
a = 0
b = 1
print(a, end = " ")
print(b, end = " ")
for i in range(2, n + 1):
     c =  a + b
     print(c, end = " ")
     a = b
     b = c

# 4. Find largest among 3 numbers.
num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print("The largest number is: ", largest)



# 5. Create Student Result System
#-	Input student details 
#-	Input marks 
#-	Calculate percentage 
#-	Display grade 
#-	Use: 
##loops 
#user input

# Student Result System
name_of_student = input("Enter Student Name: ")
roll_no_of_student = input("Enter Roll Number: ")
total_marks = 0
total_number_of_subjects = 5
for i in range(1, total_number_of_subjects + 1):
    marks = float(input("Enter marks for Subject:" + str(i) + ": "))
    total_marks += marks
percentage = total_marks / total_number_of_subjects
if percentage >= 93:
    grade = "A+"
elif percentage >= 85:
    grade = "A"
elif percentage >= 77:
    grade = "B"
elif percentage >= 69:
    grade = "C"
elif percentage >= 61:
    grade = "D"
else:
    grade = "F"
print("\nSTUDENT RESULT")
print("Name:", name_of_student)
print("Roll Number:", roll_no_of_student)
print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Grade:", grade)

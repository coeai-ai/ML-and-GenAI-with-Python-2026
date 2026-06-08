# question1 : Find sum of first 10 natural numbers.

# sum = 0
# for i in range(1, 11):
#     sum = sum + i
# print("Sum =", sum)




# Question2 : Find factorial of a number.

# num = int(input("Enter a number: "))

# fact = 1

# for i in range(1, num + 1):
#     fact = fact * i

# print("Factorial =", fact)




# Question3 : Print Fibonacci Series.

# n = int(input("Enter number of terms: "))

# a = 0
# b = 1

# print("Fibonacci Series:")

# for i in range(n):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c




# Question 4: Find largest among 3 numbers.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b and a >= c:
#     print("Largest =", a)

# elif b >= a and b >= c:
#     print("Largest =", b)

# else:
#     print("Largest =", c)




 
# Question 5:Create Student Result System
	# -	Input student details 
	# -	Input marks 
	# -	Calculate percentage 
	# -	Display grade 
	# -	Use: 
    #  if-elif-else 
    # loops 
    # user input

 # Student Details
# name = input("Enter student name: ")
# roll = input("Enter roll number: ")

# # Marks Input
# maths = int(input("Enter Maths marks: "))
# physics = int(input("Enter Physics marks: "))
# chemistry = int(input("Enter Chemistry marks: "))

# # Total and Percentage
# total = maths + physics + chemistry
# percentage = total / 3

# # Grade Calculation
# if percentage >= 90:
#     grade = "A+"

# elif percentage >= 75:
#     grade = "A"

# elif percentage >= 60:
#     grade = "B"

# elif percentage >= 40:
#     grade = "C"

# else:
#     grade = "Fail"

# # Display Result
# print("\n----- STUDENT RESULT -----")
# print("Name :", name)
# print("Roll No :", roll)
# print("Total Marks :", total)
# print("Percentage :", percentage)
# print("Grade :", grade)
#1 - Find sum of first 10 natural numbers.

# n=10
# sum=0
# for i in range(1,11,1):
#     sum=sum+i

# print("Required sum=",sum)


#2 - Find factorial of a number.

# n=int(input("Enter the number: "))
# prod=1
# for i in range(1,n+1,1):
#     prod=prod*i
# print("factorial of n is: ",prod)

#3 - Print Fibonacci Series.

# Print Fibonacci Series

# n = int(input("How many terms? "))

# a = 0
# b = 1

# print("Fibonacci Series:")

# for i in range(n):
#     print(a, end=" ")
    
#     c = a + b
#     a = b
#     b = c


#4 - Find largest among 3 numbers.

# n1=int(input("Enter number 1:"))
# n2=int(input("Enter number 2:"))
# n3=int(input("Enter number 3:"))

# if n1>n2 and n1>n3:
#     print("n1 is the largest") 
# if n2>n1 and n2>n3:
#     print("n2 is the largest") 
# if n3>n1 and n3>n2:
#     print("n3 is the largest")


"""5 - Create Student Result System
	-	Input student details 
	-	Input marks 
	-	Calculate percentage 
	-	Display grade 
	-	Use: 
if-elif-else 
loops 
user input"""

# Student Result System

# name = input("Enter student name: ")

# total = 0

# # Loop for 5 subjects
# for i in range(5):
#     marks = int(input("Enter marks: "))
#     total = total + marks

# percentage = total / 5

# # Grade calculation
# if percentage >= 90:
#     grade = "A+"
# elif percentage >= 80:
#     grade = "A"
# elif percentage >= 70:
#     grade = "B"
# elif percentage >= 60:
#     grade = "C"
# elif percentage >= 50:
#     grade = "D"
# else:
#     grade = "Fail"

# # Display result
# print("\nStudent Name:", name)
# print("Total Marks:", total)
# print("Percentage:", percentage)
# print("Grade:", grade)
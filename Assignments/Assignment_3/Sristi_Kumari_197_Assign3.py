#1-Create a function to print first 10 natural numbers

# def naturalno():
#     for i in range(1,11):
#         print(i)
# naturalno()        

#2-Create a function to calculate sum of first N natural numbers.

# def sumN(N):
#     Sum=0
#     for i in range(1,N+1,1):
#         Sum+=i
#     return Sum    
# res=sumN(5)
# print(res)

#3-Create a function to reverse a number.

# def reverse(num):
#     rev=0
#     while(num>0):
#         digit=num%10
#         rev=rev*10+digit
#         num=num//10
#     return rev
# res=reverse(90)
# print(res)

#4-Create a function to count digits in a number.

# def count(num):
#     count=0
#     while(num>0):
#         digit=num%10
#         count+=digit
#         num//=10
#     return count
# res=count(56)
# print(res)

#5-Create a function to check palindrome number.

# def palindrome(num):
#     original=num
#     rev=0
#     while (num>0):
#         digit=num%10
#         rev=rev*10+digit
#         num//=10
#         if rev==original:
#             return True
#         else:
#             return False
# res=palindrome(578)
# print(res)

#6-Create a function to generate Fibonacci series.

# def fibonacii(n):
#     a=0
#     b=1
#     for i in range(0,n+1):
#         print(a,end=" ")
#         c=a+b
#         a=b
#         b=c
# fibonacii(5)

#7-Calculator Using Functions that contains the following features;
# 	-	User selects operation 
# 	-	Program performs calculation 
# 	-	Display result

# def calculator(a,b):
#     Operation=int(input("Choose operation:\n1 for addition\n2 for subtraction\n" \
#     "3 for multiplication\n4 for division:\n"))
    
#     if(Operation==1):
#         return a+b
#     elif(Operation==2):
#         return a-b
#     elif(Operation==3):
#         return a*b
#     elif(Operation==4):
#         return a/b

# a=int(input("Enter 1st number: "))
# b=int(input("Enter 2nd number: "))
# res=calculator(a,b)
# print(res)


#8-Create a text file and store student details. 

# file = open("student.txt", "w")

# name = input("Enter student name: ")
# roll_no = input("Enter roll number: ")
# course = input("Enter course: ")

# file.write("Student Details\n")
# file.write(f"Name: {name}\n")
# file.write(f"Roll Number: {roll_no}\n")
# file.write(f"Course: {course}\n")

# file.close()

# print("Student details stored successfully in student.txt")

#9-Read data from a file. 

# with open("student.txt", "r") as file:
#     for line in file:
#         print(line.strip())

#10-Handle division by zero using exception handling. 

# try:
#     num1 = int(input("Enter numerator: "))
#     num2 = int(input("Enter denominator: "))

#     result = num1 / num2
#     print("Result:", result)

# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")

#11-Create a Student class with name and marks. 

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def display(self):
#         print("Name:", self.name)
#         print("Marks:", self.marks)


# name = input("Enter name: ")
# marks = int(input("Enter marks: "))

# student = Student(name, marks)
# student.display()
#find sum of first 10 natural numbers
sum = 0
for i in range(1, 11):
    sum += i
print("The sum of first 10 natural numbers is:", sum)

# find factorial of a number
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("The factorial of", num, "is:", factorial)

#find fibonnaci series up to n terms
n = 10
a, b = 0, 1
print("Fibonacci series up to", n, "terms:")
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
print()  # for a new line after the Fibonacci series

#find the largest among three numbers
num1 = 10
num2 = 20
num3 = 15
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print("The largest number among", num1, ",", num2, "and", num3, "is:", largest)

#create a student result system input student details ,input marks,calculate percentage,display grade:use if elif else statement
student_name = input("Enter student name: ")
student_roll = input("Enter student roll number: ")
marks = float(input("Enter marks obtained: "))
total_marks = 100
percentage = (marks / total_marks) * 100
if percentage >= 80:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "D"
print("Student Name:", student_name)
print("Student Roll Number:", student_roll)
print("Marks Obtained:", marks)
print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Grade:", grade)
total_sum = 0

for i in range(1, 11):
    total_sum += i

print(f"The sum of the first 10 natural numbers is: {total_sum}")

# Take user input
num = int(input("Enter a number to find its factorial: "))

factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is: {factorial}")

    
terms = int(input("How many terms of the Fibonacci series do you want? "))

n1, n2 = 0, 1
count = 0

if terms <= 0:
    print("Please enter a positive integer.")
elif terms == 1:
    print(f"Fibonacci series up to {terms} term:")
    print(n1)
else:
    print("Fibonacci series:")
    while count < terms:
        print(n1, end=" ")
        nth = n1 + n2
       
        n1 = n2
        n2 = nth
        count += 1
print() 


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print(f"The largest number among {num1}, {num2}, and {num3} is: {largest}")

print("--- Student Result System ---")

# Input student details
student_name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")
num_subjects = int(input("Enter the number of subjects: "))

total_marks = 0

# Loop to input marks for each subject
for i in range(1, num_subjects + 1):
    marks = float(input(f"Enter marks obtained in Subject {i} (out of 100): "))
    total_marks += marks

# Calculate percentage
max_possible_marks = num_subjects * 100
percentage = (total_marks / max_possible_marks) * 100

# Determine grade using if-elif-else
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

# Display Result Summary
print("\n" + "="*30)
print("        STUDENT REPORT        ")
print("="*30)
print(f"Name:        {student_name}")
print(f"Roll No:     {roll_number}")
print(f"Total Marks: {total_marks} / {max_possible_marks}")
print(f"Percentage:  {percentage:.2f}%")
print(f"Grade:       {grade}")
print("="*30)

# ASSIGNMENT - 2
# Find sum of first 10 natural numbers
sum = 0

for i in range(11):
    sum+=i

print("Sum of first 10 natural numbers: ", sum)

# Find factorial of a number
n = int(input("Enter number: "))
fact = 1

for i in range(1, n+1):
    fact*=i

print(f"Factorial of {n} = {fact}")

# Print Fibonacci Series
num = int(input("Enter number of terms: "))

a, b = 0, 1

print("Fibonacci Series:")

for i in range(num):
    print(a, end=" ")
    a, b = b, a + b

# Find largest among 3 numbers 
n1 = float(input("Enter 1st number: "))
n2 = float(input("Enter 2nd number: "))
n3 = float(input("Enter 3rd number: "))

if n1 >= n2 and n1 >= n3:
    print(f"{n1} is the largest number out of {n1}, {n2} and {n3}")
elif n2 >= n1 and n2 >= n3:
    print(f"{n2} is the largest number out of {n1}, {n2} and {n3}")
else:
    print(f"{n3} is the largest number out of {n1}, {n2} and {n3}")

'''
Create Student Result System
- Input student details
- Input marks
- Calculate percentage
- Display grade
- Use:
    - if-elif-else
    - loops
'''
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

subjects = ["Maths", "Science", "Computer", "English", "Data Structures"]

maths = science = computer = english = data_structures = 0

for subject in subjects:
    mark = float(input(f"Enter marks in {subject}: "))
    if subject == "Maths":
        maths = mark
    elif subject == "Science":
        science = mark
    elif subject == "Computer":
        computer = mark
    elif subject == "English":
        english = mark
    elif subject == "Data Structures":
        data_structures = mark

total = maths + science + computer + english + data_structures
percentage = (total / 500) * 100   

if percentage >= 93:
    grade = "A+"
elif percentage >= 85:
    grade = "A"
elif percentage >= 77:
    grade = "B"
elif percentage >= 69:
    grade = "C"
else:
    grade = "F"

print("\n--- Student Result ---")
print(f"Name: {name}")
print(f"Roll Number: {roll_no}")
print("Marks:")
print(f"Maths: {maths}")
print(f"Science: {science}")
print(f"Computer: {computer}")
print(f"English: {english}")
print(f"Data Structures: {data_structures}")
print(f"Total Marks = {total}")
print(f"Percentage = {percentage}%")
print(f"Grade = {grade}")


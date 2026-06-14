#Question 1: Find sum of first 10 natural numbers
total_sum = 0
for i in range(1, 11):
    total_sum = total_sum + i
print("1. Sum of first 10 natural numbers is:", total_sum)

#Question 2: Find factorial of a number
number = 5
factorial = 1
for i in range(1, number + 1):
    factorial = factorial * i
print(f"2. Factorial of {number} is:", factorial)

#Question 3: Print Fibonacci Series (First 10 numbers)
print("3. Fibonacci Series:")
n1, n2 = 0, 1
count = 0
while count < 10:
    print(n1, end=" ")
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
print()            # Just to move to a new line

#Question 4: Find largest among 3 numbers
x = 12
y = 45
z = 23
if x >= y and x >= z:
    largest = x
elif y >= x and y >= z:
    largest = y
else:
    largest = z
print("4. The largest number among 3 numbers is:", largest)

#Question 5:Create Student Result System
print("\n--- STUDENT RESULT SYSTEM ---")
name = input("Enter Student Name: ")
roll_no = input("Enter Enrollment Number: ")

# Taking marks for 3 subjects
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))

# Calculating percentage
obtained_marks = sub1 + sub2 + sub3
percentage = (obtained_marks / 300) * 100

# Finding grade using if-elif-else
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 45:
    grade = "C"
else:
    grade = "F (Needs Improvement)"

# Displaying everything
print("\n--- FINAL GRADE CARD ---")
print("Student Name:", name)
print("Enrollment Number:", roll_no)
print(f"Total Percentage scored: {percentage:.2f}%")
print("Final Grade:", grade)
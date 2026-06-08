# 1. Sum of first 10 natural numbers
sum_n = 0
for i in range(1, 11):
    sum_n += i
print("Sum of first 10 natural numbers:", sum_n)


# 2. Factorial of a number
num = int(input("\nEnter a number to find factorial: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial of", num, "is:", fact)


# 3. Fibonacci Series
n = int(input("\nEnter number of terms for Fibonacci series: "))
a, b = 0, 1

print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

print()


# 4. Largest among 3 numbers
print("\nEnter three numbers:")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)


# 5. Student Result System
print("\n--- Student Result System ---")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

subjects = int(input("Enter number of subjects: "))

total = 0

for i in range(subjects):
    marks = float(input(f"Enter marks for subject {i+1}: "))
    total += marks

percentage = (total / (subjects * 100)) * 100

print("\nStudent Name:", name)
print("Roll No:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage)

# Grade calculation
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

print("Grade:", grade)
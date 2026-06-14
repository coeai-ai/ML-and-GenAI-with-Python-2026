# 1: Find sum of first 10 natural numbers

sum = 0

for i in range(1, 11):
    sum = sum + i

print("Sum of first 10 natural numbers =", sum)


# 2: Find factorial of a number

num = int(input("\nEnter a number to find factorial: "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)


# 3: Print Fibonacci Series


n = int(input("\nEnter number of terms for Fibonacci series: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

print()

# 4: Find largest among 3 numbers

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Largest number =", a)
elif b > c:
    print("Largest number =", b)
else:
    print("Largest number =", c)


# 5: Student Result System.

name = input("\nEnter student name: ")
roll = input("Enter roll number: ")

total = 0

for i in range(1, 6):
    marks = float(input(f"Enter marks of subject {i}: "))
    total = total + marks

percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"

print("\nSTUDENT RESULT ")
print("Name:", name)
print("Roll No:", roll)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
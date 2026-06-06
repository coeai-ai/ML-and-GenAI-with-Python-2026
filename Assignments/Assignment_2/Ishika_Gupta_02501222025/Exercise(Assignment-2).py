# 1. Sum of first 10 natural numbers
sum = 0
for i in range(1, 11):
    sum += i
print("Sum of first 10 natural numbers:", sum)


# 2. Factorial of a number
num = int(input("\nEnter a number for factorial: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial =", fact)


# 3. Fibonacci Series
n = int(input("\nEnter number of terms for Fibonacci series: "))
a, b = 0, 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()


# 4. Largest among 3 numbers
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number =", largest)


# 5. Student Result System
name = input("\nEnter student name: ")
roll = input("Enter roll number: ")

#input marks of subject(out of 100) from user using for loop
total = 0
for i in range(1, 6):
    marks = float(input(f"Enter marks of Subject {i}: "))
    total += marks

percentage = (total / 500)*100

#grade is given using if-elif-else statements
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
    grade = "F"

print("\n--- Student Result ---")
print("Name:", name)
print("Roll No:", roll)
print("Percentage:", percentage)
print("Grade:", grade)
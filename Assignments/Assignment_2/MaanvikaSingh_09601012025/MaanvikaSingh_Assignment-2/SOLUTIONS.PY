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

print("Factorial is:", fact)


# 3. Fibonacci Series
n = int(input("\nEnter number of Fibonacci terms: "))

a, b = 0, 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# 4. Largest among 3 numbers
print("\n")
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
roll = input("Enter roll number: ")

marks = []
for i in range(5):
    m = int(input(f"Enter marks of subject {i+1}: "))
    marks.append(m)

total = sum(marks)
percentage = total / 5

print("\n--- RESULT ---")
print("Name:", name)
print("Roll No:", roll)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 75:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")
#1
sum = 0
for i in range(1, 11):
    sum += i
print("Sum =", sum)

#2
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial =", fact)

#3fibonacci series
n = int(input("Enter number of terms: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#4
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)

#5
name = input("Enter student name: ")
roll = input("Enter roll number: ")

total = 0
for i in range(1, 6):
    marks = float(input(f"Enter marks of subject {i}: "))
    total += marks
percentage = total / 5

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
print("\nStudent Result")
print("Name:", name)
print("Roll No:", roll)
print("Percentage:", percentage)
print("Grade:", grade)
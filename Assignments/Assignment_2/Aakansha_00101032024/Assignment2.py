# 1. Find sum of first 10 natural numbers.
sum = 0
for i in range(1, 11):
    sum += i
print("Sum of first 10 natural numbers =", sum)

# 2. Find factorial of a number.
num = int(input("Enter a number: "))
factorial = 1
for i in range(num,0,-1):
    factorial *= i
print("Factorial of", num, "=", factorial)

# 3. Print fibonacci series.
n = int(input("Enter number of terms: "))
a = 0
b = 1
print("Fibonacci Series:")
for i in range(n):
    print(a, " ")
    c = a + b
    a = b
    b = c

# 4. Find largest among 3 numbers.
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print("Largest number is:", largest)

# 5. Create Student Result System
name = input("Enter Student Name: ")
sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))
sub4 = float(input("Enter marks of Subject 4: "))
sub5 = float(input("Enter marks of Subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
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

print("\n----- RESULT -----")
print("Student Name :", name)
print("Total Marks  :", total, "/500")
print("Percentage   :", percentage, "%")
print("Grade        :", grade)

if percentage >= 50:
    print("Result       : PASS")
else:
    print("Result       : FAIL")

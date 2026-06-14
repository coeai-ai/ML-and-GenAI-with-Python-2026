#1.Sum of first 5 natural numbers
sum = 0

for i in range(1, 11):
    sum = sum + i

print("Sum of first 10 natural numbers =", sum)

#2.Factorial of a number
num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)

#3.Fibonacci Series
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    
    c = a + b
    a = b
    b = c

#4.Largest number among 3 
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if x >= y and x>= z:
    print("Largest number is", x)
elif y >= x and y>= z:
    print("Largest number is", y)
else:
    print("Largest number is", z)


#.5 Student Result System
# Input student details
name = input("Enter student name: ")
roll = input("Enter roll number: ")

# Input marks
m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))

# Calculate total and percentage
total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

# Display grade using if-elif-else
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

# Display result
print("\n----- Student Result -----")
print("Name:", name)
print("Roll Number:", roll)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)



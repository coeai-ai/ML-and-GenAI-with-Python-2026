# Find sum of first 10 natural numbers.
sum = 0
for i in range(1,11):
	sum = sum + i
print("sum of first 10 natural numbers: ",sum)	
	
# Find factorial of a number.
n = int(input("enter the num: "))
prod = 1
for i in range(1,n+1):
	prod = prod*i
print("factorial of number: ",prod)	

# Print Fibonacci Series.
num = int(input("enter the num: "))
series = 0
a = 0
b = 1
print(a,b,end=" ")
for i in range(2,num+1):
	series = a + b
	print(series,end=" ")
	a = b
	b = series
	
# Find largest among 3 numbers.
num1 = int(input("enter the num1: "))
num2 = int(input("enter the num2: "))
num3 = int(input("enter the num3: "))
if num1>num2 and num1>num3:
	print("largest number: ",num1)
elif num2>num1 and num2>num3:
	print("largest number: ",num2)
else:
	print("largest number: ",num3)
	
# Create Student Result System
# 	-	Input student details 
# 	-	Input marks 
# 	-	Calculate percentage 
# 	-	Display grade 
name = input("Enter student name: ")
m1 = float(input("Enter marks in Subject 1: "))
m2 = float(input("Enter marks in Subject 2: "))
m3 = float(input("Enter marks in Subject 3: "))
total = m1 + m2 + m3
percentage = total / 3
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
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
 

# sum of first 10 natural numbers
def sum_of_natural_numbers(n):
    if n < 1:
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)            
result = sum_of_natural_numbers(10)
print("The sum of the first 10 natural numbers is ",result)

# factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)     
number = 6
result = factorial(number)
print("The factorial of", number, "is", result)


# Fibonacci sequence
def fibonacci(n):           
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq
n = 10
result = fibonacci(n)
print("The first", n, "numbers in the Fibonacci sequence are:", result)


# largest among 3 numbers
def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
num1 = 100
num2 = 280
num3 = 11
result = largest_of_three(num1, num2, num3)                                 
print("The largest among", num1, ",", num2, "and", num3, "is", result)



# student result system
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

total = 0
subjects = ["Maths", "Science", "English", "Computer", "Hindi"]

for subject in subjects:
    marks = int(input(f"Enter marks in {subject}: "))
    total += marks

percentage = total / len(subjects)

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

print("Name       ", name)
print("Roll No.   ", roll_no)
print("Total Marks", total)
print("Percentage ", percentage, "%")
print("Grade      ", grade)
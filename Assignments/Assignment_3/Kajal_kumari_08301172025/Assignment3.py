#1. Create a function to print first 10 natural numbers
def print_natural():
    for i in range(1, 11):
        print(i)
print_natural()



#2.Create a function to calculate sum of first N natural numbers
def sum_natural(n):
    return n * (n + 1) // 2
n = int(input("Enter N: "))
print("Sum =", sum_natural(n))


#3.Create a function to reverse a number
def reverse_num(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev
num = int(input("Enter number: "))
print("Reverse =", reverse_num(num))



#4.Create a function to count digits in a number.
def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count
num = int(input("Enter number: "))
print("Digits =", count_digits(num))




#5. Create a function to check palindrome number.
def palindrome(num):
    temp = num
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return temp == rev
num = int(input("Enter number: "))
if palindrome(num):
    print("Palindrome")
else:
    print("Not Palindrome")



#6. Create a function to generate Fibonacci series.
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter number of terms: "))
fibonacci(n)

#7. Calculator Using Functions that contains the following features: User selects operation, 
# Program performs calculation ,Display result
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = int(input("Enter choice: "))
if choice == 1:
    print("Result =", add(a, b))
elif choice == 2:
    print("Result =", sub(a, b))
elif choice == 3:
    print("Result =", mul(a, b))
elif choice == 4:
    print("Result =", div(a, b))
else:
    print("Invalid Choice")



#8.Create a text file and store student details
file = open("student.txt", "w")
name = input("Enter Name: ")
roll = input("Enter Roll No: ")
file.write("Name: " + name + "\n")
file.write("Roll No: " + roll)
file.close()
print("Data Stored Successfully")


#9.Read data from a file. 
file = open("student.txt", "r")
data = file.read()
print(data)
file.close()




#10.Handle division by zero using exception handling. 
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result =", result)
except ZeroDivisionError:
    print("Division by zero is not allowed")




#11.Create a Student class with name and marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
s1 = Student("Kajal", 95)
s1.display()
#1.Creat a function to print first 10 natural number
def print_numbers():
    for i in range(1,11):
        print(i)
print_numbers()


#2.Calculate the sum of first n natural numbers:
def sum_numbers(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    print(sum)
sum_numbers(5)


#3.Create a function to reverse a number:
def reverse_number(num):
    rev=0
    while num>0:
        digit=num%10
        rev=rev* 10+ digit
        num=num//10
    print(rev)
reverse_number(123)


#4.Create a function to count digits in a number:
def count_digits(n):
    count=0
    while(n>0):
        count+=1
        n=n//10
    return count
print(count_digits(4568))


#5.Check palindrome number:
def is_palindrome(num):
    original = num
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10
    return original == reverse
num = int(input("Enter a number: "))
if is_palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
print(is_palindrome(121))


# 6.⁠ ⁠Generate Fibonacci Series

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
fibonacci(8)


# 7.⁠ ⁠Calculator Using Functions
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    return "Division by zero is not allowed"
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
print(add(4,5))
print(subtract(6,4))
print(multiply(4,5))
print(divide(100,5))


#8.⁠Create a Text File and Store Student Details
file = open("student.txt", "w")
name = input("Enter student name: ")
marks = input("Enter student marks: ")
file.write("Name: " + name + "\n")
file.write("Marks: " + marks)
file.close()
print("Student details saved successfully.")


#9.⁠Read Data from a File
file = open("student.txt", "r")
data = file.read()
print(data)
file.close()


#10.⁠Handle Division by Zero Using Exception Handling
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result =", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


#11.⁠ ⁠Create a Student Class with Name and Marks
class Student:
    def _init_(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
name = input("Enter student name: ")
marks = int(input("Enter student marks: "))
s1 = Student(name, marks)
s1.display()

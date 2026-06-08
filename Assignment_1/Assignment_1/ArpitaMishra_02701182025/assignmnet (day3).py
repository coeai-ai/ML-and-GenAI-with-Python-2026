# fUNCTION 
# func to print 10 natural numbers
def print_natural_numbers(n):
    for i in range(1,n+1):
        print(i)
n = int(input("enter the number of natural numbers you want to print:"))
print_natural_numbers(n)
#  ques 2: function to calculate the sum of first N natural numbers 
def sum_nat_numb(n):
    total = 0
    for i in range(1,n+1):
        total+= i
    return total
n = int(input("enter the number:"))
print("the sum of first", n, "natural numbers is", sum_nat_numb(n))
# que 3: function to reverse a number 
def rev_number(n):
    rev = 0
    while n > 0:
        digit = n % 10          # extract last digit
        rev = rev * 10 + digit  # build reversed number
        n = n // 10           # remove last digit
    return rev
n = 98765
print("Original number:", n)
print("Reversed number:", rev_number(n))
# que 4: funct to count digits in a number 
def count_digits(n):
    count = 0
    while n >0:
        n = n//10
        count+=1
        return count
    n = int(input("enter the number:"))
    print("the number of digits in the number is ", count_digits(n))
#  ques 5: function to check palindrome number   
def is_p(n):
    return n == rev_number(n)
n = int(input("enter the number:"))
if is_p(n):
    print(n , "is a palindrome number")
else:
    print(n , "is not a palindrome number")
# ques 6: function to generate fibbonacci series 
def generate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
n = int(input("enter the number of terms for fibonacci series:"))
print("the fibonacci series is:")
generate_fibonacci(n) 
# ques 7: calculator (user selects operation, program performs calculations, display result)
def calc():
    print("simple calculator")
    print("select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
choice = input("enter choice(1/2/3/4):")
num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))
if choice == "1":
    print(num1, "+", num2, "=",num1 + num2)
elif choice == "2":
    print(num1, "-", num2, "=",num1 - num2)
elif choice == "3":
    print(num1, "*", num2, "=",num1 * num2)
elif choice == "4":
    print(num1, "/", num2, "=",num1 / num2)
else:
    print("invalid number")
# ques 8: create a text file and store student details
f = open("student.txt","w")
name = input("enter the name")
roll_no = int(input("enter the roll number"))
marks = int(input("enter the marks"))
f.write("Name: " + name + ", Roll NO.: " + str(roll_no) + ", Marks: " + str(marks) + "\n")
f.close()
print("student details saved")
# Read data from a file
f = open("student.txt","r")
print(f.read())
f.close()
# Handle division by zero using exception handling
try:
    a = int(input('enter the numerator:'))
    b = int(input('enter the denominator:'))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
#Create a student class with name and marks
class Student:
    def __init__(self,name,roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
def display_info(self):
    print("Name:", self.name)
    print("Roll No:", self.roll_no)
    print("Marks:", self.marks)
S1 = Student("Arpita",27,95)
S1.display_info()
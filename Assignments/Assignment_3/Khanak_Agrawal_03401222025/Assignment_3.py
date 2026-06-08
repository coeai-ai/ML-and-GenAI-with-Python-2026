# q1. To print first 10 natural numbers
def natural():
    for i in range(1, 11):
        print(i, end=" ")
        
natural()


# q2. To calculate sum of first n natural numbers
def sum(n):
    ans = 0
    for i in range(1,n+1):
        ans += i
    return ans

n = int(input("\nEnter a number: "))
print("Sum of first", n, "natural numbers:", sum(n))


# q3. To reverse a number
def reverse(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n = n // 10
    return rev

num = int(input("\nEnter a number: "))
print("Reversed number:", reverse(num))


# q4. To count digits in a number
def count(n):
    cnt = 0
    while n > 0:
        cnt += 1
        n = n // 10
    return cnt

num = int(input("\nEnter number: "))
print("Number of digits in the number:", count(num))


# q5. To check palindrome number
def reverse(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n = n // 10
    return rev

def is_palindrome(n):
    return n == reverse(n)

num = int(input("\nEnter number: "))
if is_palindrome(num):
    print("It is a palindrome")
else:
    print("It is not a palindrome")


# q6. To generate fibonacci series
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        c = b
        b = a+b
        a = c

num = int(input("\nEnter number of terms: "))
fibonacci(num)


# q7. To perform operations in a calculator
def calculator(choice, a, b):
    if choice == 1:
        return a+b
    elif choice == 2:
        return a-b
    elif choice == 3:
        return a*b
    elif choice == 4:
        if b!=0:
            return a/b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid choice"

print("\n\n1.Add  2.Subtract  3.Multiply  4.Divide")
choice = int(input("Enter a choice: "))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

result=calculator(choice, a, b)
print("Result:", result)


# q8. To create a text file and store student details
def write_file():
    with open("students.txt", "w") as f:
        f.write("Name: Khanak\n")
        f.write("Roll No: 34\n")
        f.write("Course: B.Tech MAC\n")
    print("\nStudent details stored in students.txt")

write_file()


# q9. To read data from a file
def read_file():
    try:
        with open("students.txt", "r") as f:
            data = f.read()
            if data:
                print("\nContents of students.txt:")
                print(data)
            else:
                print("File is empty.")
    except FileNotFoundError:
        print("File not found.")

read_file()


# q10. To handle division by zero using exception handling
try:
    a = int(input("\nEnter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Error: Division by zero not allowed")


# q11. To create student class with name and marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("\nStudent Details")
        print("Name :", self.name)
        print("Marks:", self.marks)

name = input("\nEnter Student Name: ")
marks = float(input("Enter Student Marks: "))

s1 = Student(name, marks)
s1.display()
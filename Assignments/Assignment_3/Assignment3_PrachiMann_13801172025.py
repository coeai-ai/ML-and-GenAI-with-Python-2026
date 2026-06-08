# Create a function to print first 10 natural numbers.

def natural_numbers():
    for i in range(1, 11):
        print(i)

natural_numbers()


# Create a function to calculate sum of first N natural numbers.

def sum_of_numbers(n):
    total = 0
    
    for i in range(1, n+1):
        total += i

    return total  

n = int(input("Enter a number: "))
result = sum_of_numbers(n)
print("Sum = ", result)


# Create a function to reverse a number.

def reverse_number(num):
    rev_num = 0
    digit = 0

    while (num > 0):
        digit = num % 10;
        rev_num = (rev_num * 10) + digit
        num = num // 10
    
    return rev_num

num = int(input("Enter a number : "))
rev_num = reverse_number(num)
print("Reversed number is : ", rev_num)
    

# Create a function to count digits in a number.

def digits_in_number(num):
    count = 0

    while (num > 0):
        count += 1
        num = num // 10
    
    return count

num = int(input("Enter a number : "))
count = digits_in_number(num)
print("Digits in given number is : ", count)


# Create a function to check palindrome number.

def palindrome_or_not(num):
    original_num = num
    rev_num = 0
    digit = 0

    while (num > 0):
        digit = num % 10
        rev_num = (rev_num * 10) + digit
        num = num // 10

    if (original_num == rev_num):
        print(original_num, "is a palindrome")
    else:
        print(original_num, "is not a palindrome")

num = int(input("Enter a number : "))
palindrome_or_not(num)


# Create a function to generate Fibonacci series.

def fibonacci_series(n):
    a, b = 0, 1  
    print("Fibonacci series:")

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b   

n = int(input("Enter how many terms: "))
fibonacci_series(n)


# Calculator 

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print("Operations you can perform: \n 1.+ \n 2. - \n 3. * \n 4. / \n 5. Exit \n")
ch = int(input("Enter your choice number : "))

while (ch != 5):
    if (ch == 1):
        print("Addition result is = ", add(num1, num2))
    
    elif (ch == 2):
        print("Subtraction result is = ", subtract(num1, num2))

    elif (ch == 3):
        print("Multiplication result is = ", multiply(num1, num2))

    elif (ch == 4):
        print("Division result is = ", divide(num1, num2))

    ch = int(input("Enter your choice number : "))


# Create a text file and store student details

students = [
    "Name: A, Marks: 93\n",
    "Name: B, Marks: 85\n",
    "Name: C, Marks: 78\n"
]

with open("students.txt", "w") as f:
    f.writelines(students)

print("Student details written successfully!")


# Read data from a file 

with open("students.txt", "r") as f:
    data = f.read()
    print("File contents:\n", data)


# Handle division by zero using exception handling

try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2
    print("Result =", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")


# Create a Student class with name and marks

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name, "| Marks:", self.marks)

# Example usage
s1 = Student("A", 93)
s2 = Student("B", 85)

s1.display()
s2.display()

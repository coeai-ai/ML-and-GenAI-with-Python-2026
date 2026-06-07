## question 1
def function(x):
    for i in range(1, x + 1):
        print (i, end=' ')
function (10)


## question 2
def function(x):
    total = 0
    for i in range(1, x + 1):
        total += i
    print(total)
function(10)

## question 3
def function(x):
    for i in str(x):
        num = str(x)[::-1]
    print(num)
function(5678)


## question 4
def function(x):
    count = 0
    for i in str(x):
        count += 1
    print(count)
function(5678)


## question 5
def function(x):
    is_palindrome = True
    for i in range(len(str(x))):
        if str(x)[i] != str(x)[len(str(x)) - 1 - i]:
            is_palindrome = False
    print(is_palindrome)
function(12321)


## question 6
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
for i in range(11):
    print(fibonacci(i), end=' ')


## question 7
def operation(a,b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    
print(operation(10, 5, '+'))
print(operation(10, 5, '-'))
print(operation(10, 5, '*'))
print(operation(10, 5, '/'))    


## question 8
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
marks = input("Enter Marks: ")

with open("student.txt", "w") as file:
    file.write("Student Details\n")
    file.write(f"Name: {name}\n")
    file.write(f"Roll Number: {roll_no}\n")
    file.write(f"Marks: {marks}\n")

print("Student details stored successfully in student.txt")


# question 9
with open("student.txt", "r") as file:
    data = file.read()

print(data)


##question 10
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))

    result = a / b
    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")



## question 11
class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("name:", self.name)
        print("marks:", self.marks)

s1 = student("Alice", 85)
s1.display()            
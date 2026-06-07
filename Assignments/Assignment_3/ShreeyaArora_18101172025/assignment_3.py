#1
def first_10():
    for i in range(1,11):
        print(i,end=" ")
first_10()

#2

def sum_first_n():
    summ = 0
    print()
    n = int(input("Enter a number: "))
    for i in range(1,n+1):
        summ += i
    print(f"Sum of first {n} natural numbers is: {summ}")
sum_first_n()

#3 

def reverse(n):
    return int(str(n)[::-1])
print("Number after reversing is: ",reverse(12345))

#4

def count(n):
    return (len(str(n)))
print("Length of the number is:",count(12345))

#5

def palindrome(n):
    if n==int(str(n)[::-1]):
        print(f"{n} is a palindrome")
    else:
        print(f"{n} is not a palindrome")
palindrome(12121)

#6

def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter number of terms: "))
fibonacci(n)


#7

def calc():
    n1 = int(input("Enter first number: "))
    print()
    n2 = int(input("Enter second number: "))
    print()
    print("### Options Available ###")
    print()
    print("a = addition")
    print("s = subtraction")
    print("m = multiplication")
    print("d = division")
    print("ab = absolute difference")
    print("f = floor division")
    print()

    x = input("Enter an option from the above: ")
    if x=='a':
        return n1+n2
    elif x=='s':
        return n1-n2
    elif x=='m':
        return n1*n2
    elif x=='d':
        return n1/n2
    elif x=='ab':
        return abs(n1-n2)
    elif x=='f':
        return n1//n2
    else:
        return "Invalid option selected"

print(calc())

# 8 -  Create a text file and store student details
with open("text.txt", "w") as file:
    file.write("Name: William\n")
    file.write("Enrolment number: 121\n")
    file.write("Class: 12th\n")
    file.write("Percentage Received: 99 %")
print("Student details have been entered! ")

# 9 - Read data from a file. 
with open("text.txt", "r") as file:
    data = file.read()
print("Data of the File containing William's Details: ")
print()
print(data)

# 10 - Handle division by zero using exception handling. 
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    res = a/b
    print(f"Result is: {res}")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# 11 - Create a Student class with name and marks. 
class Student:
    def __init__(self, name,marks1,marks2):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2

    def display(self):
        print("\nStudent Details")
        print(f"Name of the student is: {self.name}")
        print(f"Marks of the student in Maths subject is: {self.marks1}")
        print(f"Marks of the student in Science subject is: {self.marks2}")

stud = Student("William",100,99)
stud.display()


    
    
    




# ASSIGNMENT-3
#1. Create a function to print first 10 natural numbers.
def Counting():
    for i in range(1,11):
        print(i)

Counting()

#2. Create a function to find the sum of first N Natural numbers.
def Sum(N):
    sum = 0
    for i in range(1,N+1):
        sum += i;
    print("Sum of first ", N, " natural numbers: ",sum)

Sum(10)    

#3. Create a function to reverse a number.
def Reverse(n):
    rev =""
    while(n>0):
        lastDigit = n%10
        rev += str(lastDigit)
        n= n//10
    print("Reverse of given number is: ", rev)

Reverse(9814)     
        
#4. Create function to count digits in a number.
def Digits(num):
    noOfDigits = 0
    while(num>0):
        noOfDigits += 1
        num = num//10
    print("Number of digits: ", noOfDigits)

Digits(123456789)    

#5. Create a function to check for a palindrome number.
def Palindrome(Num):
    temp = str(Num)
    rev =""
    while(Num>0):
        lastDigit = Num%10
        rev += str(lastDigit)
        Num = Num//10
    if(rev == temp):
        print("True")
    else: 
        print("False")  

Palindrome(121)          


#6. Create a function to generate fibonacci series.
def Fibonacci(num):
    arr = [0, 1]
    for i in range(2, num):  # start from 2!
        arr.append(arr[i-1] + arr[i-2])
    print(arr)

Fibonacci(5)    
    

#7. Create a calculator with the following features: Addition, Subtraction, Multiplication & Division.
def Calculator(numOne, numTwo, operation):
    if(operation == "+"):
        print(numOne+numTwo)
    elif(operation == "-"):
        print(numOne-numTwo) 
    elif(operation == "*"):
        print(numOne*numTwo)
    elif(operation == "/"):
        print(numOne/numTwo)
    else:
        print("Please enter a valid operation.")  

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
operation = input("Enter the operation: ")
Calculator(n1,n2,operation)


#8. Create a text file and store student's details.
def File():
    file = open("students.txt", "w")
    n = int(input("Enter number of students: "))
    for i in range(n):
        name = input("Name: ")
        roll = input("Roll No: ")
        marks = input("Marks: ")
        file.write(f"Name: {name}, Roll: {roll}, Marks: {marks}\n")
    file.close()

File()

#9. Read data from a file.
def Data():
    file = open("students.txt", "r")
    content = file.read()
    print(content)
    file.close()

Data()    

#10. Handle division by zero using exception handling. 
def Exception():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b
        print(result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

Exception()        

#11. Create a student class with name & marks.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("Rahul", 92)
s2 = Student("Priya", 88)
s1.display()
s2.display()
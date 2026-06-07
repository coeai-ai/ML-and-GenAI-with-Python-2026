#1)first 10 natural numbers
def natural_numbers():
    for i in range(1,11):
        print(i)
natural_numbers()
#2)sum of n numbers
def total(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    print(f"the sum of the numbers is=",sum)
total(3)  
#3)reverse a number
def reverse(n):
    rev=0
    while n>0:
        rev=rev*10+n%10
        n=n//10
    print(f"reversal of the number is",rev)
reverse(1234)    
#4)count digits in a number
def number(n):
    count=0
    while n>0:
        count+=1
        n=n//10
    print(f"the number of digits are=",count)
number(12345678)
#5)pallindrome
def pallindrome(n):
    rev=0
    copy=n
    while n>0:
        rev=rev*10+n%10
        n=n//10
    print(rev)
    if copy==rev:
        print("the number is pallindrone")
    else:
        print("not a pallindrome")    
pallindrome(121)
#6)fibonacci series
def fibonacci(n):
    fib1=0
    fib2=1
    for i in range(n):
        print(fib1,end=" ")
        fib3=fib1+fib2
        fib1=fib2
        fib2=fib3
fibonacci(7)
#7)Calculator
def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Choose operation: +  -  *  /")
op = input("Enter operator: ")
if op == "+":
    result = add(a,b)
elif op == "-":
    result = sub(a,b)
elif op == "*":
    result =mul(a,b)
elif op == "/":
    result = div(a,b)
else:
    result = "Invalid operator"
print("Result =", result)
#8)was to create a text file of students detail
name=input("enter you name=")
roll_number=int(input("enter your roll.number="))
marks=float(input("enter marks="))
with open("student_details.txt","a") as file:
    file.write(f"Name: {name},Roll_Number: {roll_number},Marks: {marks}")
print("file has been created")
#9)read data from the file
file=open("Student_details.txt","r")
data=file.read()
print(data)
file.close()
#10)handling division
try:
    num1=int(input("Enter your number="))
    num2=int(input("Enter your number="))
    result=num1/num2
    print(result)
except:
       print("Division not possible")
#11)student class with name and marks
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        return f"{self.name},{self.marks}"
t1 = Student("Sam", 56)
t2 = Student("Stas", 62)
t3 = Student("Xalia", 96)
print(t1.display())
print(t2.display())
print(t3.display())


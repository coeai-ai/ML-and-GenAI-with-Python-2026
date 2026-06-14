#code 1
def natural_num(n):
    for i in range(1,n+1):
        print(i,end=" ")
natural_num(10)
#code 2
def Sum(n):
    sum=0
    for i in  range(1,n+1):
        sum+=i
    print(f"Sum of the first {n} is {sum}")
n=int(input("Enter the number upto you want sum : "))
Sum(n)
#code 3
def reverse(n):
    while(n>0):
        m=n%10
        print(m,end="")
        n=n//10
n=int(input("Enter the number: "))
reverse(n)
#code 4
def count_num(n):
    count=0
    while(n>0):
        count+=1
        n=n//10
    print(count)
n=int(input("Enter the number: "))
count_num(n)
#code 5
def ispalin(n):
    original=n
    reverse=0
    while(n>0):
        m=n%10
        reverse=reverse*10+m
        n=n//10
    if(reverse==original):
      print("Palindrome")
    else:
       print("Not Palindrome")
n=int(input("Enter the number: "))
ispalin(n)
#code 6
def fibonacci(n):
    a=0
    b=1
    next=0
    for i in range(n):
        print(a,end=" ")
        next=a+b
        a=b
        b=next
n=int(input("Enter the number upto which fibonacci series is required: "))
fibonacci(n)
#code 7
def calculator(num1,num2,operation):
    if operation=="+":
        return num1+num2
    elif operation=="-":
        return num1-num2
    elif operation=="*":
        return num1*num2
    elif operation=="/":
        if num2!=0:
            return num1/num2
        else:
            print("Division not possible")
    else:
        print("Invalid operation")
num1=int(input("Enter the number one : "))
num2=int(input("Enter the number two : "))
opr=input("Enter the operation : ")
print(calculator(num1,num2,opr))
#code 8
name=input("Enter your name : ")
roll=int(input("Enter your roll number : "))
age=int(input("Enter your age : "))
with open("Student_details.txt","a") as file:
    file.write(f"Name:{name},Roll_num:{roll},Age:{age}")
print("File has been created")
#code 9
file=open("Student_details.txt","r")
data=file.read()
print(data)
file.close()
#code 10
try:
    num1=int(input("Enter the first number : "))
    num2=int(input("Enter the second number : "))
    result=num1/num2
    print(result)
except : 
    print("Division not possible")
#code 11
class Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
Name=input("Enter the name of the student : ")
marks=int(input("Enter your marks : "))
s1=Student(Name,marks)
print(s1.name)
print(s1.mark)

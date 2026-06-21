#ASSIGNMENT 3
#Swanandi Garudkar 23301012025
#Indira Gandhi Delhi Technical University for Women

#1. Create a function to print first 10 natural numbers.

def pnatural():
    for i in range(1,11):
        print(i,end=" ")
#main
pnatural()
print()

#2. Create a function to calculate sum of first N natural numbers.

def snatural(x):
    s=0
    for i in range(1,x+1):
        s+=i
    print("Sum = ",s)
#main
x=int(input("Enter the no. of terms = "))
snatural(x)

#3. Create a function to reverse a number.

def rev(n):
    n1=n
    n2=0
    while n1>0:
        d=n1%10
        n2=(n2*10)+d
        n1=n1//10
    print("The reversed no. = ",n2)
#main
x=int(input("Enter a no. to reverse = "))
rev(x)

#4. Create a function to count digits in a number.

def countn(n):
    n1=n
    c=0
    while n1>0:
        n1=n1//10
        c+=1
    print("No. of digits = ",c)
#main
x=int(input("Enter a no. = "))
countn(x)

#5. Create a function to check palindrome number.

def pal(n):
    n1=n
    n2=0
    while n1>0:
        d=n1%10
        n2=(n2*10)+d
        n1=n1//10
    if n2==n:
        print("The no. is a palindrome.")
    else:
        print("The no. is not a palindrome.")
#main
x=int(input("Enter a no. to check = "))
pal(x)

#6. Create a function to generate Fibonacci series.

def fib(x):
    t1,t2=0,1
    for i in range(x):
        print(t1,end=" ")
        t3=t1+t2
        t1=t2
        t2=t3
#main
x=int(input("Enter the no. of terms = "))
fib(x)
print()

#7. Calculator Using Functions that contains the following features;
#	-	User selects operation 
#	-	Program performs calculation 
#	-	Display result

def add(x,y):
    print("Addition = ",x+y)
def subs(x,y):
    print("Subtraction = ",x-y)
def div(x,y):
    print("Division = ",x/y)
def mult(x,y):
    print("Multiplication = ",x*y)
#main
print("Addition - 1, Subtraction - 2, Division - 3, Multiplication - 4")
x=int(input("Enter your choice = "))
a=int(input("Enter the 1st no. = "))
b=int(input("Enter the 2nd no. = "))
if x==1:
    add(a,b)
elif x==2:
    subs(a,b)
elif x==3:
    div(a,b)
else:
    mult(a,b)

#8. Create a text file and store student details. 

f=open("students.txt", "w+")
f.write("Name = Alice, Marks = 98\n")
f.write("Name = Bob, Marks = 65\n")
f.close()

#9. Read data from a file. 

f=open("students.txt", "r")
data=f.read()
print(data)

#10. Handle division by zero using exception handling. 

try:
    num=10
    den=0
    div=num/den
    print(div)
except ZeroDivisionError:
    print("Cannot divide by 0")

#11. Create a Student class with name and marks. 

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Student Name = ",self.name,", Marks = ",self.marks)
s1=student("Alex",85)
s2=student("Emma",98)
s1.display()
s2.display()









    










    

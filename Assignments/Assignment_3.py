# Question 1 Create a function to print first 10 natural numbers
def print_num(n):
    for i in range(1,n+1):
        print(i,end=" ")
        
print_num(10)
print("\n")

# Question 2 Create function to calculate sum of first 10 natural numbers 
def sum(n):
    add=0
    for i in range(1,n+1):
        add=add+i
    return(add)
print(f"the sum offirst 10 natural numbers is {sum(11)}")
print("\n")

# Question 3 Create a function to reverse a number
num=int(input ("enter number which you want to reverse: "))
def rev(num):
    revv=0
    a=num
    while(a):
       rem=a%10
       revv=revv*10+rem
       a=a//10
    return(revv)
print(f"reverse of {num} is {rev(num)}")
print("\n")

# Question 4 Create a function to count digits in it
num1=int(input("enter number to count number of digits; "))
def digit(num1):
    count=0
    while(num1):
        count+=1
        num1=num1//10
    return(count)
print(f"Number of digits present in given number is {digit(num1)} ")
print("\n")

# Question 5 Create a function to check palindrome number
num2=int(input("enter number to check if palindrome exists or not "))
# a number is called palindrome if the reverse of number is equal to the number
# method 1 usming the above reverse function
num3=rev(num2)
if(num2==num3):
    print("palindrome exist")
else:
    print("palindrome dosen't exist")
print("\n")
    
# question 6 Create a function to generate fibonacci series
def fib(n):
    a=0
    b=1
    sum=a+b
    for i in range(n):
        a=b
        b=sum
        sum=a+b
        print(sum,end=" ")
print("the required fibonacci series is: ",end=" ")
fib(5)  
print("\n")

# Question 7 Make calculator using function
op=int(input("enter '1','2','3','4' according to the function you want to perform "))
a=int(input("enter first number "))
b=int((input("enter second number ")))
def cal(op,a,b):
    print("""
          1=sum
          2=divide
          3=multiply
          4=subtract""")
    if(op==1):
        print(f"the sum of {a} and {b} is {a+b}")
    elif(op==2):
        print(f"the division of numbers is {a/b}")
    elif(op==3):
        print(f"the multiplication of numbers is {a*b}")
    elif(op==4):
        print(f"the subtraction of numbers is{a-b}")
    else:
        print("invalid input")
cal(op,a,b)
# Question 8 Create a text file and store students details
with open("students details",'w') as f:
    f.write("""Name:Naina
               Branch: CSE-AI
               Roll_No.:110""")
f.close()
# Question 9 Read data from a file
with open("students details","r") as f:
    text=f.read()
    print (text)
    f.close()
# Question 10-handle division by zero using exception handling
a=int(input("enter number which you want to divide ; "))
b=int(input("enter number by which you want to divide: "))
try:
    print(a/b)
except Exception as DivisionByZero:
    print("invalid division")
    
# Question 11 -Create a student class with name and marks
class Student:
    def student_det(self,name,marks):
        self.name=name
        self.marks=marks
s1=Student()
s1.student_det("Naina",98)
print(f"My name is {s1.name} , marks obtained in maths is {s1.marks}")

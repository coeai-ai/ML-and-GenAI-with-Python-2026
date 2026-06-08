#function to print first 10 natural numbers
def natural():
    print("First 10 natural numbers are:")
    for i  in range(1,11):
        print(i)
  #calling function  
natural()


#function to calculate sum of first N natural numbers
def sum(number):
    sum=0
    for i in range(1,number+1):
        sum+=i
    return sum

  #calling function
num=int(input("Enter number upto which you want to calculate sum:"))
sum1=sum(num)
print("Sum of first",num,"numbers is:",sum1)


#function to reverse a number
num=int(input("Enter a number:"))
def rev(num1):
    l=len(str(num1))
    reverse=0
    for i  in range(l):
        a=num1%10
        reverse=reverse*10+a
        num1//=10
    return reverse
  #calling function
rev1=rev(num)
print("Reversed number is:",rev1)


#function to count digits in a number
def count(number):
    l=len(str(number))
    return l

  #calling function
num=int(input("Enter a number:"))
length=count(num)
print("Number of digits in the given number is:",length)


#function to generate fibonacci series
def fibonacci(number):
    f1=0
    f2=1
    print(f1)
    print(f2)
    for i in range(3,number+1):
        f3=f1+f2
        print(f3)
        f1=f2
        f2=f3
  #calling function
num1=int(input("Enter the numbers of terms in Fibonacci series:"))
fibonacci(num1)

#function to check palindrome number
num=int(input("Enter a number:"))
def palin(number):
    rev2=rev(number) #calling rev function created in previous program
    if str(number)==str(rev2):
        print("Given number is Palindrome")
    else:
        print("Given number is not Palindrome")
  #calling function
palin(num)

#calculator 
def sum(a,b):
    return a+b
def diff(a,b):
    return a-b
def prod(a,b):
    return a*b
def div(a,b):
    return a/b
def rem(a,b):
    return a%b
print("//CALCULATOR//")
while True:
    num1=int(input("Enter first number"))
    num2=int(input("Enter second number:"))
    print("Choose an operation you want to perform on num1 and num2!!")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Remainder\n6.Exit")
    op=int(input("Enter operation number:"))
    if op==1:
        result1=sum(num1,num2)
        print("Sum of given two numbers is:",result1)
    elif op==2:
        result2=diff(num1,num2)
        print("Difference of given two numbers is:",result2)
    elif op==3:
        result3=prod(num1,num2)
        print("Product of given two numbers is:",result3)
    elif op==4:
        try:
            result4=div(num1,num2)
            print("Division of given two numbers is:",result4)
        except ZeroDivisionError:
            print("Division by zero is not allowed.")
    elif op==5:
        result5=rem(num1,num2)
        print("Remainder of given two numbers is:",result5)
    elif op==6:
        print("Calculator is closed.")
        break
    else:
        print("Please enter valid choice!!")


#creating text file
name=input("Enter student's name:")
roll=int(input("Enter student's roll number:"))
mark1=float(input("Enter subject 1 marks:"))
mark2=float(input("Enter subject 2 marks:"))
mark3=float(input("Enter subject 3 marks:"))
total=mark1+mark2+mark3
perc=(total/300)*100 #calculating percentage
details={"Name":name,"Roll_no":roll,"Total_marks":total,"Percentage":perc}  #putting details into dictionary
#writing details in file
try:
    with open("Student.txt","w") as f:
        f.write(str(details))
    print("File successfully created.\n")
except Exception as e:
    print("Error:",e)


#reading data from file
try:
    with open("poem.txt","r") as f:  #poem.txt file is there is in the same folder as this py file
        contents=f.read()
        print("File is opened successfully.")
        print(contents)
except Exception as e:
    print("Error:",e)

#exception handling
num1=float(input("Enter Numerator:"))
num2=float(input("Enter Denominator:"))
try:
    result=num1/num2
    print("Result is:",result)
except ZeroDivisionError:
    print("Error:Division by zero is not allowed.")


#student class
class student:
    def __init__(self,name,mark1,mark2,mark3):
        self.name=name
        self.total=mark1+mark2+mark3
    def display(self):
        print("Name of students is:",self.name)
        print("Total marks of student is:",self.total)

name1=input("Enter student's name:")
m1=float(input("Enter subject 1 marks:"))
m2=float(input("Enter subject 2 marks:"))
m3=float(input("Enter subject 3 marks:"))
s=student(name1,m1,m2,m3)
s.display()



    









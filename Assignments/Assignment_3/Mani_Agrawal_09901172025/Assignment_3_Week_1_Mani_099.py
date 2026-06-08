# Question 1 - Create a function to print first 10 natural numbers.
def naturalNumber():
    for i in range(1,11):
        print(i)
# function call
naturalNumber()

# Question 2 - Create a function to calculate sum of first N natural numbers.
def sumNaturalNumber(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
# function call
sumNumber=sumNaturalNumber(10)
print(f"Sum of first 10 natural number is {sumNumber}")

# Question 3 - Create a function to reverse a number.
def reverseNumber(num):
    revNum=0
    while(num>0):
        a=num%10
        revNum+=a
        revNum*=10
        num/=10
        num=int(num)
    revNum/=10
    revNum=int(revNum)
    return revNum
# function call
number=int(input("Enter number:"))
rev=reverseNumber(number)
print(f"Reverse of {number} is {rev}")

#                                                             OR
def reverseNumber(num):
    numStr=str(num)
    revNum=int(numStr[::-1])
    return revNum
# function call
number=int(input("Enter number:"))
rev=reverseNumber(number)
print(f"Reverse of {number} is {rev}")

#Question 4 - Create a function to count digits in a number.
def countDigit(num):
    numString=str(num)
    return len(numString)
# function call  
number=int(input("Enter number:"))
numOfDigit=countDigit(number)
print(f"Number of digit in {number} is {numOfDigit}")

# Question 5 - Create a function to check palindrome number.
def checkPalindrome(num):
    numStr=str(num)
    revNum=int(numStr[::-1])
    if(num==revNum):
        return True
    else:
        return False
# function call
number=int(input("Enter number:"))
IsPalindrome=checkPalindrome(number)
print(f"Is the number {number} palindrome: {IsPalindrome}")

# Question 6 - Create a function to generate Fibonacci series.
def fibonacciSeries(num):
    listFibo=[0,1]
    if(num==1):
        return listFibo[0]
    if(num==2):
        return listFibo[1]
    for i in range(0,num-2):
        num=listFibo[i]+listFibo[i+1]
        listFibo.append(num)
    return listFibo
# function call
fiboUpto1=fibonacciSeries(1)
fiboUpto10=fibonacciSeries(10)
print(f"Fibonacci series upto 1 number is {fiboUpto1}")
print(f"Fibonacci series upto 10 number is {fiboUpto10}")

# Question 7 - Calculator Using Functions that contains the following features
            #    User selects operation 
		    #    Program performs calculation 
		    #    Display result

def select2Num():
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    return num1,num2
def selectOperation():
    print("Choose opearation to perform:")
    print("1 : Additon")
    print("2 : Subtraction")
    print("3 : Multiplication")
    print("4 : Division")
    print("5 : Modulus")
    print("6 : power")
    number=int(input("Enter number of the operation to perform:"))
    return number
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def division(num1,num2):
    if(num2==0):
        return "cannot divide by zero"
    else:
        return num1/num2
def modulus(num1,num2):
    if(num2==0):
        return "cannot divide by zero"
    else:
        return num1%num2
def power(num1,num2):
    return num1**num2
def calculation(number1,number2,chosenOperation):
    if(chosenOperation==1):
        result=add(number1,number2)
        print(f"Sum of the numbers is {result}")
    elif(chosenOperation==2):
        result=sub(number1,number2)
        print(f"Difference of the numbers is {result}")
    elif(chosenOperation==3):
        result=multiply(number1,number2)
        print(f"Multiply of the numbers is {result}")
    elif(chosenOperation==4):
        result=division(number1,number2)
        print(f"Division of the numbers is {result}")
    elif(chosenOperation==5):
        result=modulus(number1,number2)
        print(f"Remainder will be {result}")
    elif(chosenOperation==6):
        result=power(number1,number2)
        print(f"{number1} raised to the power {number2} is {result}")
    else:
        print("Invalid operation chosen")

# function call
first,second=select2Num()
operation=selectOperation()
calculation(first,second,operation)

# Question 8 - Create a text file and store student details. 
with open("student.txt","a") as file:
    name=input("Enter student Name:")
    rollNo=int(input("Enter roll number:"))
    collegeName=input("Enter college name:")
    file.write(f"Student Name : {name}\n")
    file.write(f"Roll Number : {rollNo}\n",)
    file.write(f"College Name : {collegeName}\n")

# Question 9 - Read data from a file. 
with open("student.txt","r") as file:
    data=file.read()
    print(data)

# Question 10 - Handle division by zero using exception handling. 
try:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    div=num1/num2
    print(f"Division of {num1} by {num2} will be {div}")
except ZeroDivisionError:
    print("You cannot divide by zero")
finally:
    print("Program completed")

# Question 11 - Create a Student class with name and marks.
class Student():
    def __init__(self):
        self.studentName=input("Enter student name:")
        self.marks=float(input("Enter student marks:"))
# object of the class
student1=Student()
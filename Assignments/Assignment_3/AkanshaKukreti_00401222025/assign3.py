#ASSIGNMENT 03

#Create a function to print first 10 natural numbers.
def question1():
    print("The first 10 natural no.s: ")
    for i in range(0,10):
        print(i+1,end=" ,")

#Create a function to calculate sum of first N natural numbers.
def sumNum(n):
    sum=0
    for i in range(0,n):
        sum+=i+1
    print("The sum of first",n,"natural numbers.: ",sum)

x=int(input("Enter no.: "))
sumNum(x)

#Create a function to reverse a number.
def reverseNum(n):
    num=0
    while n>0:
        r=n%10
        n=n//10
        num=num*10+r
    return num
print(reverseNum(67953))

#Create a function to count digits in a number.
def digitCount(n):
    count=0
    while n>0:
        count+=1
        n=n//10
    return count
print("No of digits is: ",digitCount(37826))

#Create a function to check palindrome number.
def palindrome(a):
    myNum=str(a)
    is_pali=False
    for i in range(0,len(myNum)//2):
        if myNum[i]==myNum[len(myNum)-i-1]:
            is_pali=True
        else: 
            is_pali=False
    if is_pali==True:
        print("Yes! a palindrome")
    elif is_pali==False:
        print("No! Not a palindrome")
palindrome(1647498)
palindrome(13431)

#Create a function to generate Fibonacci series.
def fibonacci():
    n=int(input("Enter no. of elements in fibonacci: "))
    start1=0
    start2=1
    print(start1,end=", ")
    print(start2,end=", ")
    for i in range(0,n-2):
        start3=start1+start2
        print(start3,end=", ")
        start1=start2
        start2=start3

#Calculator Using Functions that contains the following features;
#- User selects operation
#- Program performs calculation
#- Display result
def calculator(x,y):
    print("Enter (1) for Addition \n (2) for Subtraction \n (3) for Multiplication \n (4) for Division \n")
    option=int(input("Enter option no.: "))
    if (option==1):
        return x+y
    elif(option==2):
        return x-y  
    elif(option==3):
        return x*y
    elif(option==4):
        return x/y
    else:
        print("Wrong input") 

print(calculator(8,5))
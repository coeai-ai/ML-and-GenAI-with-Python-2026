#ASSIGNMENT 02

#Find sum of first 10 natural numbers.
def question1():
    sum=0
    for i in range(1,11):
        sum=sum+i
    print("Sum of First 10 natural no.s: ",sum)

#Find factorial of a number.
def question2():
    n=int(input("Enter a no.: "))
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("Factorial of ",n," is: ",fact)

#Print Fibonacci Series.
def question3():
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
        
#Find largest among 3 numbers.
def question4():
    x=int(input("Enter num.: "))
    y=int(input("Enter another num.: "))
    z=int(input("Enter another num.: "))
    if(x>y and x>z):
        print("Largest is :",x)
    elif(y>z):
        print("Largest is :",y)
    else:
        print("Largest is :",z)

#Create Student Result System :Input student details-Input marks- Calculate percentage-Display gradeUse:- if-elif-ese- loops
def question5():
    #student details
    name=input("Enter your name: ")
    branch=input("Enter your branch: ")
    #student marks
    marks={}
    print("Enter your marks of 5 subj (out of 100): ")
    total_m=0
    for i in range(0,5):
        marks[i]=int(input("marks: "))
        total_m=total_m+marks[i]
    percentage=(total_m/500)*100
    print("Percentage: ",float(percentage),"%")

    #Checking grade
    if percentage>90:
        print("Grad: A")
    elif percentage>80:
        print("Grade: B+")
    elif percentage>73:
        print("Grade: B")
    elif percentage>60:
        print("Grade: C")
    else :
        print("Grade F")


question1()
question2()
question3()
question4()
question5()
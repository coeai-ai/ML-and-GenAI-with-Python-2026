#ASSIGNMENT 2
#Swanandi 23301012025

#1. Find sum of first 10 natural numbers.

s=0
for i in range(1,11):
    s+=i
print("Sum of first 10 natural numbers = ",s)

#2. Find factorial of a number.

x=int(input("Enter a no. = "))
f=1
for i in range(1,x+1):
    f*=i
print("Factorial = ",f)

#3. Print Fibonacci Series.

x=int(input("Enter the no. of terms = "))
t1,t2=0,1
for i in range(x):
    print(t1,end=" ")
    t3=t1+t2
    t1=t2
    t2=t3
print()

#4. Find largest among 3 numbers.

a=int(input("Enter the 1st no. = "))
b=int(input("Enter the 2nd no. = "))
c=int(input("Enter the 3rd no. = "))
l=max(a,b,c)
print("The largest no. = ",l)

#5. Create Student Result System
#	-	Input student details 
#	-	Input marks 
#	-	Calculate percentage 
#	-	Display grade 

for i in range(1,4):
    print("STUDENT ",i)
    n=input("Enter the students name = ")
    maths=float(input("Enter maths marks = "))
    science=float(input("Enter science marks = "))
    per=(maths+science)/2
    print("Name = ",n)
    print("Percentage = ",per)
    if per>90:
        print("Grade = A")
    elif per<90 and per>70:
        print("Grade = B")
    elif per<70 and per>50:
        print("Grade = C")
    else:
        print("Grade = F")

















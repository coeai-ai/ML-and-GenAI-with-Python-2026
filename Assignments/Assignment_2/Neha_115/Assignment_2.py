#Q1. Find sum of first 10 natural numbers.
for i in range(1,11):
    print(i)

# Q2. Find factorial of a number.
n=int(input("enter the number:"))
if n<0:
    print("factorial is not define")
else:
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("factorial of",n,":",fact)


# Q3. Print Fibonacci Series.
n=int(input("enter number:"))
a=0
b=1
for i in range(n):
    print(a, end=" ")
    c=a+b
    a=b
    b=c

# Q4. Find largest among 3 numbers.
n1=int(input("enter number 1:"))
n2=int(input("enter number 2:"))
n3=int(input("enter number 3:"))
print(n1," ",n2," ",n3)
if n1>=n2 and n1>=n3:
    print(n1," is the greatest")
elif n2>n1 and n2>n3:
    print(n2,"is the greatest")
else:
    print(n3,"is the greatest")

"""Q5. Create Student Result System
- Input student details - Input marks - Calculate percentage - Display grade - Use: if-elif-else loops user input"""
name=input("enter the name of student:")
mark_phy=int(input("enter the marks of physics:"))
mark_maths=int(input("enter the marks of maths:"))
marks_chem=int(input("enter the marks of chemistry:"))
percentage=((mark_phy+mark_maths+marks_chem)/3)
print("percentage:",percentage)
if percentage>=90:
    print("grade:A+")
elif percentage>=80:
    print("grade:A")
elif percentage>=70:
    print("grade:B+")
else:
    print("grade:B")
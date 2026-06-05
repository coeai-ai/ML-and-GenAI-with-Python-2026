# sum of first 10 natural numbers 
sum=0
for i in range(1,11):
    sum=sum+i
print("Sum of sirst 10 natural number is ", sum)

# find factorial of a number
fact=1
n=int(input("Enter the number "))
for i in range(1,n+1):
    fact=fact*i
print("Fcatorial of a number is ",fact)

# print fibonacci seeries 

a=0
b=1
number=int(input("Enter the number "))
print ()
for i in range(n+1):
    print(a, end=" ")
    a, b = b, a + b

# to find largest among 3 numbers 
a =int(input("Enter the first number "))
b =int(input("Enter the second number "))
c =int(input("Enter the third number "))
if a>b and a>c :
    print ("A is greatest")
elif b>c and b>a:
    print("B is greatest")
else:
    print ("C is greatest")


# to create student result system 

name =input("Enter the name of student ")
first=float(input("Enter the marks of student "))
second=float(input("Enter the marks of student "))
third=float(input("Enter the marks of student "))
total=first+second+third
percentage=total/3
print("The percentage of the stdent is ", percentage)

if percentage>90:
    print("Grade = A+")
elif percentage>80:
    print("Grade= A ")
elif percentage>70:
    print("Grade= B+ ")
elif percentage>60:
    print("Grade= B ")
elif percentage>50:
    print("Grade= C ")
elif percentage>40:
    print("Grade= D ")
else:
    print("Fai ")









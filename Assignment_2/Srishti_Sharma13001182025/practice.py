#code 1
sum=0
for i in range(1,11):
    sum+=i
print(f"Sum of first 10 natural numbers is {sum}")
#code 2
n=int(input("Enter the number to find the factorial: "))
pro=1
for i in range(1,n+1):
    pro=pro*i
print(f"The factorial of {n} is {pro}")
#code 3 
n=int(input("Enter the number for fibonacci series : "))
a=0
b=1
for i in range(0,n):
    print(a,end=" ")
    next=a+b
    a=b
    b=next 
#code 4
n1=int(input("Enter the first number : "))
n2=int(input("Enter the second number : "))
n3=int(input("Enter the third number : "))
if(n1>n2):
    if(n1>=n3):
        print(f"{n1} is the largest")
    else:
        print(f"{n3} is the largest")
elif(n2>n1):
    if(n2>n3):
        print(f"{n2} is the largest")
    else:
        print(f"{n3} is the largest")
else:
    print("All are equal")
#code 5
Name=input("Enter your name : ")
Roll_num=int(input("Enter your roll number : "))
Class=int(input("Enter your class : "))
total=int(input("Enter the total marks of all subjects : "))
subj1=int(input("Enter your marks of subject one : "))
subj2=int(input("Enter your marks of subject two : "))
subj3=int(input("Enter your marks of subject three : "))
subj4=int(input("Enter your marks of subject four : "))
subj5=int(input("Enter your marks of subject five : "))
sum=subj1+subj2+subj3+subj4+subj5
per=(sum/total)*100
print(f"Percentage obtained is {per}")
if(per>90):
    print("Your Grade is A")
elif(80<per<90):
    print("Your Grade is B")
else:
     print("Your Grade is C")
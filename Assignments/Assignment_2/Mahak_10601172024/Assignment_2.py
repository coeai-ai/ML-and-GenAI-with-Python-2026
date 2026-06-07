# Question 1
sum=0
for i in range(1, 11):
    sum+=i
print("Sum of first 10 Natural Numbers :",sum)


# Question 2
fac=1
n=5
for i in range(1,n+1):
    fac*=i
print("Factorial of",n,"is :",fac)


# Question 3
first=0
second=1
print("First 7 elements of fibonacci series:-")
print(0)
print(1)
for i in range(5):       #fibonacci series of length 7
    fib=first+second
    print(fib)
    first=second
    second=fib


# Question 4
a=5
b=3
c=9
if a>b and a>c:
    print(a,"is the greatest")
elif b>a and b>c:
    print(b,"is the greatest")
else:
    print(c,"is the greatest")


# Question 5
Physics=int(input())     
Chemistry=int(input())    
Maths=int(input())        
Total_Marks=Physics+Chemistry+Maths
Percentage=(Total_Marks*100)/300
if Percentage>=93:                                 #grade based on percentage
    print("Your Percentage is",Percentage,"% and Your grade is A+")
elif Percentage>=85:
    print("Your Percentage is",Percentage,"% and Your grade is A")
elif Percentage>=77:
    print("Your Percentage is",Percentage,"% and Your grade is B+")
elif Percentage>=69:
    print("Your Percentage is",Percentage,"% and Your grade is B")
elif Percentage>=61:
    print("Your Percentage is",Percentage,"% and Your grade is C+")
elif Percentage>=53:
    print("Your Percentage is",Percentage,"% and Your grade is C")
else:
    print("Your Percentage is",Percentage,"% and Your grade is D")
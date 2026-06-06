# Find sum of first 10 natural numbers.
sum=0
for i in range(1,11):
    sum+=i
print("Sum of first 10 natural number = ",sum)


# Find factorial of a number.
n=int(input("Enter a number : "))
fact=1
for i in range(1,n+1):
    fact*=i
print("Factorial of the number is : ",fact)


# Print Fibonacci Series.
n=int(input("Enter the number of fibonacci terms : "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print("\n")


# Find largest among 3 numbers.
num1=int(input("Enter number 1 : "))
num2=int(input("Enter number 2 : "))
num3=int(input("Enter number 3 : "))
if(num1>num2 and num1>num3):
    print("Number 1 is largest")
elif(num2>num1 and num2>num3):
    print("Number 2 is largest")
elif(num3>num2 and num3>num1):
    print("Number 3 is largest")


# Create Student Result System
name=input("Enter your name : ")
roll_number=input("Enter your roll number : ")
english=int(input("Enter your english marks : "))
hindi=int(input("Enter your hindi marks : "))
maths=int(input("Enter your maths marks : "))
science=int(input("Enter your science marks : "))
percent=(english+hindi+maths+science)/4
print("Your percentage is : ",percent)
if(percent>=90 and percent<=100):
    print("You scored grade A")
elif(percent>=70 and percent<90):
    print("You scored grade B")
else:
    print("You scored grade C")


"""
Below is the output I got after running the program:

Sum of first 10 natural number =  55
Enter a number : 6
Factorial of the number is :  720
Enter the number of fibonacci terms : 10
0 1 1 2 3 5 8 13 21 34 

Enter number 1 : 13
Enter number 2 : 9
Enter number 3 : 5
Number 1 is largest
Enter your name : radha
Enter your roll number : 161
Enter your english marks : 98
Enter your hindi marks : 92
Enter your maths marks : 85
Enter your science marks : 95
Your percentage is :  92.5
You scored grade A
"""

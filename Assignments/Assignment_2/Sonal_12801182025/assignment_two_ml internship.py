#1)sum of 1st 10 numbers
sum=0
for i in range(1,11):
    sum+=i
print(f"the sum upto 1st 10 natural number is:",sum)    
#2)factorial of a number
n=int(input("enter the number="))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(f"the factorial of the number is=",fact)    
#3)print fibonacci series
n=int(input("enter the number of terms u want in the series="))
fib1=0
fib2=1
print("Fibonacci seies:")
for i in range(n):
    print(fib1, end="")
    fib3=fib1+fib2
    fib1=fib2
    fib2=fib3

#4)largest among three numbers
a=int(input("enter the first number="))
b=int(input("enetr the 2nd number="))
c=int(input("enter the 3rd number="))
if(a>b and a>c):
    print(f"the greatest amongst the 3 is=",a)
elif(b>a and b>c):
    print(f"the greatest amongst the three is=",b)
else:
    print(f"the greatest amongst three is=",c) 

#5)Student Result System
student_name=input("enter student's name=")
roll_number=int(input("enter the roll number="))
student_class=int(input("enter the class="))
subject=int(input("enter number of subject"))     
total_marks=0
for i in range(subject):
    marks=float(input(f"enter marks for subject {i+1}:"))
    total_marks+=marks 
percentage=total_marks/subject  
if percentage>=90:
    grade="A+"
elif percentage>=80:
    grade="A"    
elif percentage>=70:
    grade="B"  
elif percentage>=60:
    grade="C"    
elif percentage>=50:
    grade="D"  
else:
    garde="F"
print(f"Name:",student_name)
print(f"Class:",student_class)  
print(f"Roll number:",roll_number)
print(f"Total marks:",total_marks)
print(f"Percentage:",percentage)
print(f"Grade:",grade)




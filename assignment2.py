#1 : find sum of first 10 natural numbers
sum=0
for i in range(1,11):
    sum=sum+i
print("The sum of first 10 natural numbers is : ",sum)

#2 : find the factorial of a number
num=int(input("Enter the number "))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print("The factorial of", num, "is", factorial) 

#3 : print fibonacci series up to n terms
n=int(input("Enter the number of terms "))  
a=0
b=1
if n==1:
    print(a)
elif n==2:
    print(a,b)
else:
    print(a,b,end=" ")
    for i in range(2,n):
        c=a+b
        print(c,end=" ")
        a=b
        b=c

#4 : find the largest of 3 numbers
num1=float(input("Enter the first number "))
num2=float(input("Enter the second number "))
num3=float(input("Enter the third number "))
if num1>=num2 and num1>=num3:
    largest=num1
elif num2>=num1 and num2>=num3:
    largest=num2
else:
    largest=num3
print("The largest number is : ",largest)  

#5 : create student result system- input student name, roll number, marks of 5 subjects and calculate percentage and grade
name=input("Enter student name ")
roll_no=input("Enter student roll number ") 
s1=float(input("Enter first subject marks "))
s2=float(input("Enter second subject marks "))  
s3=float(input("Enter third subject marks "))
s4=float(input("Enter fourth subject marks "))
s5=float(input("Enter fifth subject marks "))
total_marks=s1+s2+s3+s4+s5
percentage=total_marks/5    
if percentage>=90:
    grade='A'
elif percentage>=80:
    grade='B'
elif percentage>=70:
    grade='C'
elif percentage>=60:
    grade='D'
else:
    grade='F'

print("Student Name: ", name)
print("Roll Number: ", roll_no)
print("Total Marks: ", total_marks)
print("Percentage: ", percentage)
print("Grade: ", grade)
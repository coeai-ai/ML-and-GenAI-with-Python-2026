# QUESTION 1 
sum = 0
for i in range(1,11):
    sum+=i
print(" sum of first 10 natural numbers is = " , sum)

# QUESTION 2
num = int(input("Enter the number :> "))
fact = 1
for i in range(1,num+1):
    fact = fact*i
print("Factorial of the given number = " , fact)

# QUESTION 3
a = 0
b = 1
n = int(input("Enter the number of fibonacci series :>"))
print (a,b, end = " ")
for i in range(n):
    res = a  + b
    a = b
    b = res
    print(res , end = " ")

# QUESTION 4
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
if( a>b and a>c):
    print(f"{a} is greatest")
elif(b>a and  b>c):
    print(f"{b} is greatest")
else:
    print(f"{c} is greatest")


#QUESTION 5
print("----- Student Result System -----")
name = input("Student's name: ")
roll_no = input("Student's roll no: ")
total_marks = 0
for i in range(1,7):
    marks = int(input(f"Enter marks of subject {i} : "))
    total_marks += marks
percentage = (total_marks/600)*100
print(f"percentage = {percentage}")
if(percentage <= 100 and percentage>=90):
    print(f"Grade = {"A"}")
elif(percentage<90 and percentage >=80):
    print(f" Grade = { "B"}")
elif(percentage<80 and percentage >=70):
    print(f" Grade = { "C"}")
elif(percentage<70 and percentage >=60):
    print(f" Grade = { "D"}")
elif(percentage<60 and percentage >= 50):
    print(f" Grade = { "E"}")
else:
    print("Grade = F (FAIL)")

#



    

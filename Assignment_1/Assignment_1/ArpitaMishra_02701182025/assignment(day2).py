# sum of first 10 natural numbers
total = 0 
for i in range(1,11):
    total+= i
    print("sum of first ten nat numbers",total)
    
# find factorial of a number
numb = int(input("enter the no."))
factorial = 1
if numb < 0:
    print("factorial does not exist")
elif numb == 0:
    print("factorial is equal to 1")
else:
    for i in range (1,numb+1):
        factorial = factorial*i
        print("the factorial of a",numb,"is",factorial)        
# print fibbonacci series
n = int(input("enter the no."))
a = 0
b = 1
c = 0
for a in range(n):
        print(c)
        a = b
        b = c
        c = a + b
# find largest among three numbers
n1 = int(input("enter the first no."))
n2 = int(input("enter the second no."))
n3 = int(input("enter the third no."))
if n1>n2 and n1>n3:
    print("first number ", n1,"is greater among all")
elif n2>n1 and n2>n3:
    print("second number ", n2,"is greater among all")
else:    
    print("third number ", n3,"is greater among all")
# create student result system 
# (input student det, input marks,cal percen,display grade,using if elif else,loops)
name = input("enter your student's name:")
roll_no = int(input("enter the enrollment number:"))
mark1 = float(input("Enter marks of subj 1"))
mark2 = float(input("Enter marks of subj 2"))
mark3 = float(input("Enter marks of subj 3"))
mark4 = float(input("Enter marks of subj 4"))
mark5 = float(input("Enter marks of subj 5"))

total = mark1+mark2+mark3+mark4+mark5
percentage = total/5*100
# grade system 
if percentage >= 93:
    print("your grade is A+")
elif percentage >= 78:
    print("your grade is B+")
elif percentage >= 65:
    print("your grade is B")    
elif percentage >= 57:
    print("your grade is C+")    
else:
    print("failed")    


print("Name is",name)
print("Rollno. is",roll_no)
print("marks is",mark1, mark2, mark3)
print("Total is ",total)
print("Percentage", percentage,"%")

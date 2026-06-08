#exercise-2
#print 1-10 numbers
for i in range (1,11):
    print(i) #vertically
    print(i ,end=" ")  #horizantally

#first 10 even numvbers
for j in range (2,2*11,2):
    print(j)

#Multiplication Table
print("multiplication table")
num=int(input("Enter number:"))
for i in range (1,11):
    print(num , "x" , i ,"=", num*i)

#vote
print("\nCheck eligibility of vote here: \n")
age= int(input("Enter age :"))
if int(age)>=18:
    print("Eligible to vote\n")
else :
    print("not eligible to vote\n")

#display grade based on marks
print("Check yore grade here__IGDTUW grading system")
marks=int(input("Enter marks:"))
if marks<45:
    print("Grade: F")
elif 45<=marks<=52:
    print("Grade: D")
elif 45<=marks<=60:
    print("Grade: C")
elif 45<=marks<=68:
    print("Grade: C+")
elif 45<=marks<=76:
    print("Grade: B")
elif 45<=marks<=84:
    print("Grade: B+")
elif 45<=marks<=92:
    print("Grade: A")
elif 45<=marks<=100:
    print("Grade: A+")

#factorial of a number:
print("enter a number to find the factorial")
fac=int(input("Enter number:"))
num=1
for i in range(fac,1,-1):
    num=num *i
print (num)

#reverse a number
print("Magic reversal")
num=input("Enter the number:")
x=len(num)
y=int(num)
for i in range (0,x):
    a=y//(10**i)
    print ("Reversed number:",a % 10 , end="" )


#alternate method and easy way
print("\nReversed string:",num[::-1])









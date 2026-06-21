# Find sum of first 10 natural numbers.
s = 0
for i in range(11):
 s+=i
print("The sum of first 10 natural no.s",s)

# Find factorial of a number.
n = int(input("Enter any no.:"))
s = 1
for i in range(1,n+1,1):
 s*=i
print("Factorial is:",s)

# Print Fibonacci Series.
# Find largest among 3 numbers.
a = int(input("Enter first no.:"))
b = int(input("Enter second no.:"))
c = int(input("Enter third no.:"))
if a>b & a>c:
 print("a is the greatest")
elif b>a & b>c:
  print("b is the greatest")
else:
  print("c is the greatest")

# student result system
n=int(input("Enter no. of elements in fibonacci: "))
start1=0
start2=1
print(start1,end=", ")
print(start2,end=", ")
for i in range(0,n-2):
    start3=start1+start2
    print(start3,end=", ")
    start1=start2
    start2=start3


# taking input for students details
#student details
name=input("Enter your name: ")
branch=input("Enter your branch: ")
#student marks
marks={}
print("Enter your marks of 5 subj (out of 100): ")
total_m=0
for i in range(0,5):
    marks[i]=int(input("marks: "))
    total_m=total_m+marks[i]
percentage=(total_m/500)*100
print("Percentage: ",float(percentage),"%")

#Checking grade
if percentage>90:
    print("Grad: A")
elif percentage>80:
    print("Grade: B+")
elif percentage>73:
    print("Grade: B")
elif percentage>60:
    print("Grade: C")
else :
    print("Grade F")



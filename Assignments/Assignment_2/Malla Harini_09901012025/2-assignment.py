#print 1-10 numbers
sum=0
for i in range (1,11):
    sum=sum+i
    print(sum)

#factorial of a number:
print("enter a number to find the factorial")
fac=int(input("Enter number:"))
num=1
for i in range(fac,1,-1):
    num=num *i
print (num)

#fibonacci series
a=int(input("Enter first num of series:"))
b=int(input("Enter next num of series:"))
length=int(input("length of the series:"))

print(a, b, end=" ")

for i in range(2,length):   #already 2 num are printed
   next_num=a+b
   print(next_num, end=" ")
   a,b=a,next_num

#largest among three number
e=int(input("Enter first num of series:"))
f=int(input("Enter next num of series:"))
g=int(input("Enter third num of series:"))

if e>f and e>g:
   print(e,"is the largest number")
elif f>g and f>e:
   print(f,"is the largest number")
else:
   print(g,"is the largest number")

# Student Result System

# Input number of students
total_students = int(input("Total number of students: "))

# Input maximum marks for each subject
each = int(input("Max marks for each subject: "))

# Loop through each student
for s in range(total_students):
    # Input student details
    student_name = input("\nEnter Student name: ")
    sub1 = int(input("Enter marks of subject 1: "))
    sub2 = int(input("Enter marks of subject 2: "))
    sub3 = int(input("Enter marks of subject 3: "))
    sub4 = int(input("Enter marks of subject 4: "))
    sub5 = int(input("Enter marks of subject 5: "))

    # Calculate total and percentage
    total = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = (total * 100) / (each * 5)

    # Display report card
    print("\n------ Report Card of", student_name, "------")
    print("Total Marks:", total)
    print(f"Percentage: {percentage:.2f}%")

    # Display grade based on percentage
    print("Check your grade here__IGDTUW grading system")

    if percentage < 45:
        print("Grade: F")
    elif 46 <= percentage <= 52:
        print("Grade: D")
    elif 53 <= percentage <= 60:
        print("Grade: C")
    elif 61 <= percentage <= 68:
        print("Grade: C+")
    elif 69 <= percentage <= 76:
        print("Grade: B")
    elif 77 <= percentage <= 84:
        print("Grade: B+")
    elif 85 <= percentage <= 92:
        print("Grade: A")
    elif 93 <= percentage <= 100:
        print("Grade: A+")

    print("-------------------------------\n")


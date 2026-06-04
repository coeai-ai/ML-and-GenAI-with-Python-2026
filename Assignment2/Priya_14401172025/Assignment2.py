#1.Find the sum of first 10 natural numbers
sum=0
for i in range(1,11):
    sum=sum+i
print("Sum:",sum)


#2.Find the factorial of a number
n=5
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial:",fact)


#3.Print the fibonacci series
n=8
a,b=0,1
for i in range(n):
    print(a,end=" ")
    temp=a
    a=b
    b=temp+b
print()

#4.Find largest among three numbers
a=10
b=15
c=8
if(a>b and a>c):
    print("a is largest")
elif(b>a and b>c):
    print("b is largest")
else:
    print("c is largest")


#5.Create Student result system
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
subjects = int(input("Enter Number of Subjects: "))
obtained_marks = 0
for i in range(subjects):
    marks = float(input(f"Enter marks for Subject {i + 1}: "))
    obtained_marks += marks
total_marks = subjects * 100
percentage = (obtained_marks / total_marks) * 100
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"
#Display Result
print("\n----- RESULT -----")
print("Name:", name)
print("Roll No:", roll_no)
print("Obtained Marks:", obtained_marks)
print("Total Marks:", total_marks)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)


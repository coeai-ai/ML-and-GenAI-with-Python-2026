# Question 1 - Find sum of first 10 natural numbers.
num=10
sumOf10NaturalNum=0
for i in range(1,num+1):
    sumOf10NaturalNum+=i
print(f"Sum of 10 natural number is {sumOf10NaturalNum}")

# Question 2 - Find factorial of a number.
num=int(input("Enter number:"))
factorial=1
for i in range(2,num+1):
    factorial*=i
print(f"Factorial of {num} is {factorial}")

#Question 3 - Print Fibonacci Series.
fibonacciSeries=[0,1]
num=int(input("Enter the number of fibonacci series element you want:"))
if(num==1):
    print(0)
elif(num==2):
    print(fibonacciSeries)
else:
    for i in range(0,num-2):
        newNum=fibonacciSeries[i]+fibonacciSeries[i+1]
        fibonacciSeries.append(newNum)
    print(fibonacciSeries)

# Question 4 - Find largest among 3 numbers.
num1=float(input("Enter number 1 : "))
num2=float(input("Enter number 2 : "))
num3=float(input("Enter number 3 : "))
if(num1>=num2 and num1>=num3):
    print(f"{num1} is largest among the 3 numbers.")
elif(num2>=num3):
    print(f"{num2} is largest among the 3 numbers.")
else:
    print(f"{num3} is largest among the 3 numbers.")

# Question 5 - Create Student Result System:
# Student Report
studentName=input("Enter name of the student:")
rollNo=int(input("Enter roll no.:"))
subjectNumber=int(input("Enter number of subjects student has:"))
totalMarks=0
for i in range(subjectNumber):
    mark=float(input("Enter marks:"))
    totalMarks+=mark
percentage=totalMarks/(subjectNumber*100)*100
print(f"Percentage is {percentage}")
if(percentage>=85):
    print("Grade is A")
elif(percentage>75):
    print("Grade is B")
else:
    print("Grade is C")
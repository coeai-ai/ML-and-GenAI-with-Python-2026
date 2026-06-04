# ASSIGNMENT:2
#1. Find the sum of first 10 natural numbers.
sum = 0
for i in range(1,11):
    sum+=i
print("The sum of first 10 natural numbers is: ",sum)

#2. Find the factorial of a number.
n = int(input("Enter the number you want to find factorial of: "))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print("The factorial of the required number is: ",fact)  

#3. Print Fibonacci Series.
num = int(input("Enter the number of elements you want to print in the Fibonacci Series: "))
arr = [0,1]
for i in range(1,num-1):
    arr.append(arr[i]+arr[i-1])
print(arr)    

#4. Find the largest among 3 numbers.
numOne = int(input("Enter first number: "))
numTwo = int(input("Enter second number: "))
numThree = int(input("Enter three numbers: "))
if(numOne>numTwo and numOne>numThree):
    print(numOne)
elif(numTwo>numThree):
    print(numTwo)
else:
    print(numThree)   

#5. Create student result system: Input student details, input marks, calculate percentage, display grade, use: if-elif-else and loops
name = input("Enter your name: ")
rollNumber = int(input("Enter roll number: "))
noOfSubjects = int(input("Enter total number of subjects: "))
sum = 0
for i in range(1 , noOfSubjects+1):
    marks = int(input("Enter marks: "))
    sum += marks

percentage = (sum/noOfSubjects)
print("Your percentage is: ", percentage)

if(percentage>90):
    print("Grade A")
elif(percentage>70):
    print("Grade B")
elif(percentage>50):
    print("Grade C")
elif(percentage>30):
    print("Grade D")
else:
    print("Fail")        




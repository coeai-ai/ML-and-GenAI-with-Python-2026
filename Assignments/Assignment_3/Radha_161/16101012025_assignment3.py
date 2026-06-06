# Create a function to print first 10 natural numbers.
def naturalNum():
    for i in range(1,11):
        print(i,end="  ")
naturalNum()
print("\n")

# Create a function to calculate sum of first N natural numbers.
def sumN(N):
    if(N==0):
        return 0
    else:
        return N+sumN(N-1)
print("Sum of first 5 natural numbers is",sumN(5))

# Create a function to reverse a number.
def reverse(num):
    ans=0
    while(num>0):
        digit=num%10
        num=num//10
        ans=(ans*10)+digit
    return ans
print("Reverse of 1524 is",reverse(1524))

# Create a function to count digits in a number.
def countDigits(num):
    count=0
    while(num>0):
        num=num//10
        count+=1
    return count
print("Number of digits in 15240 is",countDigits(15240))

# Create a function to check palindrome number.
def checkPalindrome(num):
    newnumber=reverse(num)
    if(num==newnumber):
        return 1
    else:
        return 0
print("The number 152363251","is" if checkPalindrome(152363251) else"is not","a palindrome.")

# Create a function to generate Fibonacci series.
def Fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
Fibonacci(10)
print("\n")

# Calculator Using Functions that contains the following features;
# 	-	User selects operation 
# 	-	Program performs calculation 
# 	-	Display result
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def divide(a,b):
    return a/b
num1=int(input("Enter a number : "))
num2=int(input("Enter another number : "))
operation=int(input("Choose an operation to be performed" "\n"\
"1. Add\n" \
"2. Subtract\n" \
"3. Multiply\n" \
"4. Divide\n"))
if(operation==1):
    print(add(num1,num2))
elif(operation==2):
    print(sub(num1,num2))
elif(operation==3):
    print(multi(num1,num2))
elif(operation==4):
    print(divide(num1,num2))

# Create a text file and store student details
with open("student.txt", "w") as file:
    file.write("Name: Radha\n")
    file.write("Marks: 95\n")
print("Student details stored in file.")

# Read data from a file. 
with open("student.txt", "r") as file:
    data = file.read()
print("Data from file:",data)

# Handle division by zero using exception handling. 
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Create a Student class with name and marks. 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Radha", 95)
s1.display()

"""
I got the following result after running the program:

1  2  3  4  5  6  7  8  9  10  

Sum of first 5 natural numbers is 15
Reverse of 1524 is 4251
Number of digits in 15240 is 5
The number 152363251 is a palindrome.
0 1 1 2 3 5 8 13 21 34 

Enter a number : 9
Enter another number : 8
Choose an operation to be performed
1. Add
2. Subtract
3. Multiply
4. Divide
1
17
Student details stored in file.
Data from file: Name: Radha
Marks: 95

Enter numerator: 9
Enter denominator: 8
Result = 1.125

Student Details
Name: Radha
Marks: 95
"""
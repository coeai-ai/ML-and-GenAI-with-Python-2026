#1  Create a function that prints the first 10 natural numbers.
def Printfirst():
    for i in range (1,11):
        print(i)
Printfirst()

#2 Create a function to calculate sum of first N natural numbers.
def SumOfM(m):
    sum=0
    for i in range(m+1):
        sum+=i
    return sum

n= int(input("Enter a number:"))
print("The sum of the first", n, "natural numbers is:", SumOfM(n))

#3 Create a function to reverse a number.
def ReverseNum(n):
    rev=0

    while n>0:
        digit= n%10
        rev= rev*10 + digit
        n= n//10
    print("The reverse of the number is:", rev)
n= int(input("Enter a three digit number:"))
ReverseNum(n)

#4 Create a function to find the length of a number.
def LengthOfNum(n):
    print("The Length of the number is:", len(str(n)))

n= int(input("Enter a n digit number: "))
LengthOfNum(n)

#5 Create a function to check palindrome number.
def Palindrome(num):
    rev=0
    temp=num
    while temp>0:
        digit= temp%10
        rev= rev*10 + digit
        temp= temp//10
    if num==rev:
        print("The number is a palindrome.")

n= int(input("Enter a three digit number:"))
Palindrome(n)

#6 
def Fibonacci(n):
    a,b= 0,1
    for i in range(n+1):
        print(a, end=' ')
        a,b= b, a+b

n= int(input("Enter the number of terms for Fibonacci sequence:"))
Fibonacci(n)

#7 Calculator Using Functions that contains the following features;
	# -	User selects operation 
	# -	Program performs calculation 
	# -	Display result

def Calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", num1 + num2)
    elif choice == '2':
        print(num1, "-", num2, "=", num1 - num2)
    elif choice == '3':
        print(num1, "*", num2, "=", num1 * num2)
    elif choice == '4':
        if num2 != 0:
            print(num1, "/", num2, "=", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid input")

Calculator()

#8 Create Text File and Store Student Details
n= int(input("Enter the number of students:"))
with open("student_details.txt", "w") as file:
    for i in range(n):
        name= input("Enter the student's name:")
        eng= int(input("Enter marks for English:"))
        maths= int(input("Enter marks for Maths:"))
        science= int(input("Enter marks for Science:"))
        file.write("Student Name: " + name + "\n")
        file.write("Marks for English: " + str(eng) + "\n")
        file.write("Marks for Maths: " + str(maths) + "\n")
        file.write("Marks for Science: " + str(science) + "\n")

#9 Read Data from a text file
with open("student_details.txt", "r") as file:
    data = file.read()
    print(data)

#10 Handle division by zero using exception handling. 
def SafeDivision(num1, num2):
    try:
        result = num1 / num2
        print("The result of division is:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))
SafeDivision(num1, num2)

#11 Create a Student class with name and marks. 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)


#12 Create objects of the Student class and display their details.
student1 = Student("Aman", 85)
student2 = Student("Billy", 90)

student1.display()
student2.display()






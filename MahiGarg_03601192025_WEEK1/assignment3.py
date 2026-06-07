#Create a function to print first 10 natural numbers.
def print10() :
    for i in range(1,11) :
         print(i)
         print()
print10()


#Create a function to calculate sum of first N natural numbers.
def printn(n) :
     sum=0
     for i in range(1,n+1) :
          sum+=i
     print(sum)
printn(6)


#Create a function to reverse a number.
def reverse(n) :
     rev=0
     while(n!=0) :
          rem=n%10
          rev = rev*10 + rem
          n=n//10
     print(rev)
reverse(345)


#Create a function to count digits in a number.
def count(n) :
     c=0
     while(n!=0) :
          n=n//10
          c+=1
     print(c)
count(3456)


#Create a function to check palindrome number.
def palindrome(n):
     temp=n
     rev=0
     while(n!=0) :
          rem=n%10
          rev = rev*10 + rem
          n=n//10
     if(rev==temp) :
        print("Palindrome")
     else :
        print("Not Palindrome")
palindrome(12321)


#Create a function to generate Fibonacci series.
def fibonacci(n) :
     a=0
     b=1
     print(a,end=" ")
     print(b,end=" ")
     for i in range(2,n) :
          c=a+b
          print(c,end=" ")
          a=b
          b=c
fibonacci(10)


#Calculator Using Functions that contains the following features;
#	-	User selects operation 
#	-	Program performs calculation 
#	-	Display result
def add(a,b) :
        return a+b
def subtract(a,b) :
        return a-b
def multiply(a,b) :
        return a*b
def divide(a,b) :
        return a/b
print("Select operation.")
op=input("enter + for addition, - for subtraction, * for multiplication, / for division: ")
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if op=="+" :
        print(add(a,b))
elif op=="-" :  
        print(subtract(a,b))
elif op=="*" :
      print(multiply(a,b))
elif op=="/" :
      print(divide(a,b))
else :
      print("Invalid operator")


#Create a text file and store student details. 
file = open("students.txt", "w")
file.write("Name: John Doe, Marks: 85\n")
file.write("Name: Jane Smith, Marks: 92\n")
file.write("Name: Alice Johnson, Marks: 78\n")
file.close()


#Read data from a file. 
file = open("students.txt", "r")
data = file.read()
print(data)


#Handle division by zero using exception handling. 
def divide(a,b) :
     try :
          result=a/b
          print(result)
     except ZeroDivisionError :
          print("Cannot divide by zero")
divide(10,0)


#Create a Student class with name and marks
class Student :
     def __init__(self,name,marks) :
          self.name=name
          self.marks=marks
     def display(self) :
            print("Name:",self.name)
            print("Marks:",self.marks)

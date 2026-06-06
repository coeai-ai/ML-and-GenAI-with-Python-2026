# Assignment 3
# 1. 
def firsten():
   sum = 0
   for i in range (1,11):
       sum+=i
   print('Sum of first 10 numbers:',sum)   
firsten()

#2.
def firstn(n):
   sum = 0
   for i in range (1,n):
      sum+=i
   print('Sum of first',n,'natural numbers is:',sum)
firstn(20)

#3.
def reverse(a):
   reversenum=str(num)[::-1]
   print('number after reversing is :',reversenum)
num=int(input('Enter a number :'))
reverse(num)

#4. 
def countd(num1):
   print('Number of digit:',len(str(abs(num1))))
digit=int(input('Enter a digit:'))
countd(digit)

#5.
def palindrome(num):
   if str(num)==str(num)[::-1]:
      print('It is Palindromic number')
   else:
      print('Not a Palindromic number')
n=int(input('Enter a number:'))
palindrome(n)
      
#6.
def fibonacci():
   a = 0
   b = 1
   c = int(input('Enter till how many terms you want to print the fibonacci Series:'))
   for i in range(c):
    print(a,end=" ")
    a,b= b,a+b
fibonacci()

#7.
print('Calculator')
def add(a,b):
   return a+b
def sub(a,b):
   return a-b
def mult(a,b):
   return a*b
def div(a,b):
   return a/b
def mod(a,b):
   return a%b
p=float(input('Enter a number1 :'))
q=float(input('Enter a number2:'))
c=int(input('Enter choice from (1/5):'))


if c==1:
 print('add',add(p,q))
elif c==2:
   print('sub',sub(p,q))
elif c==3:
   print('multiplication',mult(p,q))
elif c==4:
  print('division',div(p,q))
elif c==5:
   print('Modulo',mod(p,q))
else:
   print('Enter valid choice')

#8.
with open("student.txt","w") as file:
   file.write("Alice:90\nBob:85")
#9.
with open("student.txt","r") as file:
   content = file.read()
print(content)
#10. 
try:
   num = 10/0
except ZeroDivisionError:
   print("Error you can not divide ny zero.")
#11.
class Student:
   def __init__(self,name,marks):
      self.name = name
      self.marks = marks
      
s1= Student("Ani",95)
print('Student:',s1.name,'Marks:',s1.marks)
 

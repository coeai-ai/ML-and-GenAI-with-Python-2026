#1.Find sum of first 10 natural numbers
sum = 0
for i in range (1,11):
  sum+=i
print(sum)
print('')
print('')
#2. Find factorial of a number
fact = 1
num=5
if num< 0 :
  print('No Factorial')
elif num==0 :
  print('factorial is 1')
else:
  for i in range(1,num+1):
    fact=fact*i 
  print('The Factorial of',num,'is:',fact)
print('')
print('')
#3. Print Fibonacci Series
a = 0
b = 1
c = int(input('Enter till how many terms you want to print the fibonacci Series:'))
for i in range(c):
  print(a,end=" ")
  a,b= b,a+b
print('')
print('')
#4. Find largest among three numbers
num1 = int(input("Enter a number1 :"))
num2 = int(input("Enter a number2 :"))
num3 = int(input("Enter a number3 :"))
if num1>num2 and num1>num3 :
  print(num1 ,"is the largest among three numbers")
elif num2>num1 and num2>num3:
  print(num2 ,"is the largest among three numbers")
else:
  print(num3 ,"is the largest among three numbers")
print('')
print('')
#5. Create Student Result System
name = input('enter student name :')
std = int(input('enter student standard :'))
rollno = int(input('enter student rollno. :'))
print('Enter marks of student out of 100 in each subject')
e=float(input("Enter english marks :"))
m=float(input("Enter mathematics marks :"))
h=float(input("Enter hindi marks :"))
s=float(input("Enter science marks :"))
ss=float(input("Enter socialscience marks :"))
total = e+m+h+s+ss
percentage = total/5
if percentage>=90:
  print("Grade A")
elif percentage<90 and percentage>=75:
  print("Grade B")
elif percentage<75 and percentage>=60:
  print('Grade C')
elif percentage<60 and percentage>33:
 print('Grade D')
else  :
  print('Grade E')
print("        Student Result         ")
print('Student Name:',name)
print('Class:',std)
print('Roll no.:',rollno)
print("Percentage",percentage,'%')


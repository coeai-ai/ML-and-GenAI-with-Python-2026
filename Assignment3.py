# Question1
def natural_no():
  for i in range(1,11):
    print(i)

natural_no()

# Question2
def sum_of_no(N):
  sum = 0
  for i in range(1,N+1):
    sum += i
  print(sum)

sum_of_no(8)

# Question3
def reverse_no(a,b):
  a,b = b,a
  print(a,b)

reverse_no(4,5)

# Question4
def count_digits(n):
  count = 0
  while n>0:
    count+= 1
    n//= 10
  return count

n = int(input("Enter the Number:"))
print("Digits:",count_digits(n))

# Question5
def palindrome(n):
  temp = n
  rev = 0
  while n>0:

    digit = n % 10
    rev = rev*10 + digit
    n//= 10
  return temp == rev

num = int(input("Enter Number:"))

if palindrome(num):
  print("Palindrome")

else:
  print("Not Palindrome")

#Question6
def fibo_series(n):
  fibo = [0,1]
  for i in range(2,n):
    fibo.append(fibo[i-1]+fibo[i-2])
  print(fibo)

n = int(input("Enter Number: "))
fibo_series(5)

# Question7
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1.Add 2.Subtract 3.Multiply 4.Divide")
choice = int(input("Enter choice: "))

if choice == 1:
    print(add(a, b))
elif choice == 2:
    print(sub(a, b))
elif choice == 3:
    print(mul(a, b))
elif choice == 4:
    print(div(a, b))
else:
    print("Invalid Choice")

# Question8

name = input("Enter name: ")
marks = input("Enter marks: ")

with open("student.txt", "w") as file:
 file.write("Name: " + name + "\n")
 file.write("Marks: " + marks)

 file.close()

print("Data stored successfully.")

# # Question 9
file = open("student.txt", "r")

data = file.read()
print(data)

file.close()

# Question 10
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))

    result = a / b
    print(result)

except ZeroDivisionError:
    print("Division by zero is not allowed.")

# Question 11
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Rocky", 90)
s1.display()



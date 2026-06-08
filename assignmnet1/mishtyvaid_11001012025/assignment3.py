#1. create a function to print first 10 natural numbers
def natural():
  print("The first 10 natural numbers are: ")
  for i in range(1,11):
    print(i)

natural()


#2. function to calculate sum of first N natural numbers
def sum_natural(N):
  sum=0
  if N<1:
    print("Please enter a number greater than 1")
    return
  else:
    for i in range(1,N+1):
      sum+=i
  return sum


N=int(input('Enter a positive number:'))
print(sum_natural(N))


#3. create a function to reverse a number
def reverse(num):
  STR=str(num)
  rev=int(STR[::-1])
  return rev

num=int(input('Enter a number: '))
print(reverse(num))


#4. create a function to count digits in a number
def count_digits(num):
  STR=str(num)
  count=0
  for i in STR:
    count+=1
  return count

num=int(input("Enter a number: "))
print("The number of digits in the given entry: ",count_digits(num))
     

#5. function to check palindrome number
def palindrome(num):
  STR=str(num)
  rev=int(STR[::-1])
  if num==rev:
    print("The given number is a palindrome")
  else:
    print("The given number is NOT a palindrome")

num=int(input("Enter a number: "))
palindrome(num)
     


#6. a function to generate fibonacci series
def fibonacci(n):
  num1=0
  num2=1
  for i in range(n):
    print(num1, end=" ")
    num1,num2=num2, num1+num2

n=int(input("Enter the number of entries you want in this fibonacci series: "))
fibonacci(n)


#7. function for a calculator
def addition(n):
    total = 0
    for i in range(1, n + 1):
        num = float(input("Enter number " + str(i) + ": "))
        total += num
    return total

def subtraction(n):
    total = 0
    for i in range(1, n + 1):
        num = float(input("Enter number " + str(i) + ": "))
        if i == 1:
            total = num
        else:
            total -= num
    return total

def multiply(n):
    total = 1
    for i in range(1, n + 1):
        num = float(input("Enter number " + str(i) + ": "))
        total *= num
    return total

def divide(n):
    total = 0
    for i in range(1, n + 1):
        num = float(input("Enter number " + str(i) + ": "))
        if i == 1:
            total = num
        else:
            if num == 0:
                print("Cannot divide by zero, skipping.")
                continue
            total /= num
    return total

def main():
    print("MENU")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = int(input("Enter your choice: "))
    n = int(input("Enter the number of entries: "))
    if choice == 1:
        print("Result:", addition(n))
    elif choice == 2:
        print("Result:", subtraction(n))
    elif choice == 3:
        print("Result:", multiply(n))
    elif choice == 4:
        print("Result:", divide(n))
    else:
        print("Invalid choice")

main()



#8. create txt file and store student details
file=open('student.txt', 'w')
file.write("Name\t| Roll No.\n")
file.write("_____________________\n")
file.write("Anushka\t| 1\n")
file.write("Ridima\t| 2\n")
file.write("Nitya\t| 3\n")
file.close()

print("txt file made successfully")


#9. read data from a file
file= open('student.txt', 'r')
print(file.read())


#10. handle division by 0 using exception handling
try:
    num1=int(input("Enter dividend: "))
    num2=int(input("Enter divisor: "))
    result=num1/num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid integers only.")


#11. create a student class with name and marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Anushka", 95)
s2 = Student("Ridima", 88)
s3 = Student("Nitya", 76)
s1.display()
print("_____________________")
s2.display()
print("_____________________")
s3.display()


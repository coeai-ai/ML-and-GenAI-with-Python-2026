def natural_nos():
    for i in range(1, 11):
         print(i)
natural_nos()


def sum_naturalnos():
    sum=0
    for i in range(1,11):
        sum=sum+i
    print(sum)
sum_naturalnos()

def reverse_number(num):
   reversed_num = 0
   while num > 0:
       digit = num % 10          
       reversed_num = (reversed_num * 10) + digit
       num = num // 10              
       return reversed_num
print(reverse_number(12345))


def count_digits(number):
   positive_number = abs(number)
   return len(str(positive_number))

print(count_digits(6789))

def palindrome(t):
    s = str(t)
    return s == s[::-1]
print(palindrome("racecar"))

def fibonacci(n):
    a, b = 0, 1
    l = []
    for i in range(n):
        l.append(a)
    a, b = b, a + b
    return l
print(fibonacci(10))



file = open("student.txt", "w")

name = input("Enter student name: ")
roll = input("Enter roll number: ")
marks = input("Enter marks: ")

file.write(f"Name: {name}\n")
file.write(f"Roll No: {roll}\n")
file.write(f"Marks: {marks}\n")

file.close()

print("Student details stored successfully.")



file = open("student.txt", "r")

data = file.read()
print("File Contents:")
print(data)

file.close()

try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))

    result = num1 / num2
    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


s1 = Student("Ananya", 95)


s1.display()    

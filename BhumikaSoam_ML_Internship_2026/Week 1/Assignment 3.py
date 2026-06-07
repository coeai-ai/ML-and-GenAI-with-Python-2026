#1-Print first 10 natural nums
def ten_naturals():
    num = 1
    while num <= 10:
        print(num, "\t")
        num += 1

ten_naturals()


#2-Sum of first N natural nums
def sum_n_naturals(n):
    sum = 0
    for x in range(1, n + 1):
        sum += x
    print("The sum of first", n, "natural numbers is : ", sum)

sum_n_naturals(7)


#3-Reverse a number
def reverse_num(num):
    rev = 0
    while num > 0:
        remainder = num % 10
        rev = (rev * 10) + remainder
        num = num // 10
    print("Reversed number:", rev)

reverse_num(5691)


#4-Count digits in a number
def count_digits(num):
    count = 0
    if num == 0:
        count = 1
    else:
        while num > 0:
            count += 1
            num = num // 10
    print("Total digits:", count)

count_digits(5627823)


#5-Check palindrome number
def check_palindrome(num):
    temp = num
    reverse = 0
    while temp > 0:
        remainder = temp % 10
        reverse = (reverse * 10) + remainder
        temp = temp // 10
    if num == reverse:
        print("YES! It is a palindrome number")
    else:
        print("NO!, It is not a palindrome number")

check_palindrome(78987)


#6-Generate Fibonacci series
def fibonacci(count):
    prev = 0
    curr = 1
    print("Elements of fibonacci series:")
    if count >= 1:
        print(prev)
    if count >= 2:
        print(curr)
    for x in range(count - 2):
        prev, curr = curr, prev + curr
        print(curr)

fibonacci(22)


#7-Calculator Using Functions
def add(a, b):
    print("Sum:", a + b)

def subtract(a, b):
    print("Diff:", a - b)

def multiply(a, b):
    print("Prod:", a * b)

def divide(a, b):
    if b == 0:
        print("Division by zero is not possible!")
    else:
        print("Quotient:", a / b)

def calculator():
    print("Select operation:")
    print("1 : Add")
    print("2 : Subtract")
    print("3 : Multiply")
    print("4 : Divide")
    choice = input("Enter choice : ")
    
    num1 = int(input("Enter num1 : "))
    num2 = int(input("Enter num2 : "))
    
    if choice == '1':
        add(num1, num2)
    elif choice == '2':
        subtract(num1, num2)
    elif choice == '3':
        multiply(num1, num2)
    elif choice == '4':
        divide(num1, num2)
    else:
        print("Invalid Choice")

calculator()
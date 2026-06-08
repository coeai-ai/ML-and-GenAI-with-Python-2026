# #Question 1 : Create a function to print first 10 natural numbers.

# def print_numbers():
#     for i in range(1, 11):
#         print(i)

# print_numbers()




# #Question 2 : Create a function to calculate sum of first N natural numbers.

# def sum_natural(n):
#     total = 0

#     for i in range(1, n + 1):
#         total += i

#     return total

# n = int(input("Enter N: "))
# print("Sum =", sum_natural(n))



# # Question 3 : Create a function to reverse a number.

# def reverse_number(num):
#     rev = 0

#     while num > 0:
#         digit = num % 10
#         rev = rev * 10 + digit
#         num = num // 10

#     return rev

# num = int(input("Enter a number: "))
# print("Reversed Number =", reverse_number(num)) 




# # Question 4 : Create a function to count digits in a number.

# def count_digits(num):
#     count = 0

#     while num > 0:
#         count += 1
#         num = num // 10

#     return count

# num = int(input("Enter a number: "))
# print("Number of digits =", count_digits(num))




# # Question 5 : Create a function to check palindrome number.

# def palindrome(num):
#     original = num
#     rev = 0

#     while num > 0:
#         digit = num % 10
#         rev = rev * 10 + digit
#         num = num // 10

#     if original == rev:
#         print("Palindrome Number")
#     else:
#         print("Not a Palindrome Number")

# num = int(input("Enter a number: "))
# palindrome(num)




# # Question 6 : Create a function to generate Fibonacci series.

# def fibonacci(n):
#     a = 0
#     b = 1

#     for i in range(n):
#         print(a, end=" ")
#         c = a + b
#         a = b
#         b = c

# n = int(input("Enter number of terms: "))
# fibonacci(n)




#  # Question 7 : Calculator Using Functions that contains the following features;
#-	User selects operation 
#	-	Program performs calculation 
#	-	Display result

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     return a / b

# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")

# choice = int(input("Enter your choice: "))

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# if choice == 1:
#     print("Result =", add(a, b))

# elif choice == 2:
#     print("Result =", subtract(a, b))

# elif choice == 3:
#     print("Result =", multiply(a, b))

# elif choice == 4:
#     print("Result =", divide(a, b))

# else:
#     print("Invalid Choice")
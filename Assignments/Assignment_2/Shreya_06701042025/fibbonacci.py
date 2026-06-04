# Program to print Fibonacci series

# Input number of terms
n = int(input("Enter number of terms: "))

# First two terms
a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
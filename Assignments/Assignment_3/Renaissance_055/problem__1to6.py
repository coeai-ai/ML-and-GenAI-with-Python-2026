#1. Function to print first 10 natural numbers
def print_10_numbers():
    for i in range(1, 11):
        print(i, end=" ")
    print()
#2. Function to calculate sum of first N natural numbers
def calculate_sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
#3. Function to reverse a number 
def reverse_num(num):
    return int(str(num)[::-1])
#4. Function to count digits in a number 
def count_digits(num):
    return len(str(num))
#5. Function to check palindrome number
def is_palindrome(num):
    return num == reverse_num(num)
#6. Function to generate Fibonacci series
def generate_fibonacci(terms):
    n1, n2 = 0, 1
    for _ in range(terms):
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
    print()

print("1. First 10 Natural Numbers:")
print_10_numbers()
print("\n2. Sum of first 5 natural numbers:")
print(calculate_sum_n(5))
print("\n3. Reverse of 1234:")
print(reverse_num(1234))
print("\n4. Count digits in 78965:")
print(count_digits(78965))
print("\n5. Is 121 a palindrome?")
print(is_palindrome(121))
print("\n6. Fibonacci series (first 8 terms):")
generate_fibonacci(8)
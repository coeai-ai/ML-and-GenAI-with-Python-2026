def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev

num = int(input("Enter a number: "))
print("Reversed Number =", reverse_number(num))
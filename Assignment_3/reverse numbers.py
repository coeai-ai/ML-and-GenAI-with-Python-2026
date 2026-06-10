def reverse_number(num):
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    print("Reversed Number =", rev)

num = int(input("Enter a number: "))
reverse_number(num)
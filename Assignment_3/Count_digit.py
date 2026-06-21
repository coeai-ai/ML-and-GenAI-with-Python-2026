def count_digits(num):
    count = 0

    while num > 0:
        count = count + 1
        num = num // 10

    print("Number of digits =", count)

num = int(input("Enter a number: "))
count_digits(num)
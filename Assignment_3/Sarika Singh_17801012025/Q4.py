def countDigits(n):
    count = 0

    while n > 0:
        n = n // 10
        count += 1

    return count

num = int(input("enter a number"))
print("Number of digits =", countDigits(num))
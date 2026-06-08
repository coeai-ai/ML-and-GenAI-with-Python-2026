def sum_natural(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total

n = int(input("Enter N: "))
print("Sum =", sum_natural(n))
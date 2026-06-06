# print fibonacci series
n = int(input("Enter number of terms: "))
a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = b
    b = a+b
    a = c
def reverse(n):
    s=0
    while(n>0):
        r=n%10
        n=n//10
        s=(s+r)*10
    return s//10
num=int(input("Enter a number: "))
ans=reverse(num)
print(ans)

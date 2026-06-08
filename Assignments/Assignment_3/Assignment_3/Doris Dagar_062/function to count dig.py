def count_dig(n):
    x=n
    count=0
    while(x>0):
        count+=1
        x=x//10
    return count
num=int(input("Enter a number: "))
ans=count_dig(num)
print(ans)
def check_palindrome(n):
    x=n
    s=0
    while(x>0):
        r=x%10
        x=x//10
        s=(s+r)*10
    s=s//10
    if(s==n):
        print("Yess",n,"is a palidrome")
    else:
        print("Noo",n,"is not a palindrome")
num=int(input("Enter a number: "))
check_palindrome(num)
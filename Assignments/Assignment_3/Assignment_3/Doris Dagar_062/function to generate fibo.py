def generate_fibo(n):
    a=0
    b=1
    print(a,end=' ')
    for i in range(n-1):
       print(b,end=' ')
       tmp=a+b
       a=b
       b=tmp
num=int(input("Enter the number of terms: "))
generate_fibo(num)
sum=0
for i in range(1,11,1):
    sum=sum+i
print(sum)

fact=1
n = int(input("Enter the value of n:"))
for i in range(1,n+1,1):
    fact = fact*i
print(fact)


n=int(input("Enter the value for n:")) 
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

a = int(input('Enter the value for a:'))
b = int(input('Enter the value for b:'))
c = int(input('Enter the value for c:'))
if(a>b and a>c):
    print("a is the largest")
elif(b>a and b>c):
    print("b is the largest")
else:
    print("c is the lasrgest")


name = input("Enter the name:")
marks= int(input('Enter the marks scored out of 100:'))
if(marks>90 and marks<=100):
    print("O Grade")
elif(marks>80 and marks<=90):
    print("E Grade")
elif(marks>70 and marks<=80):
    print("A Grade")
elif(marks>60 and marks<=70):
    print("B Grade")
elif(marks>50 and marks<=60):
    print("C Grade")
elif(marks>40 and marks<=50):
    print("D Grade")
else:
    print("Fail")




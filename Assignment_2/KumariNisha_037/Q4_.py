#Find largest among 3 numbers

a=int(input("the first no. :"))
b=int(input("the second no. :"))
c=int(input("the third no. :"))

if a>b:
    if a>c:
        print("the largest among three is ",a)
    else:
        print("the largest among three is",c)

else:
    if b>c:
     print("the largest among three is ",b)
    else :
       print("the largest among three is",c)
       
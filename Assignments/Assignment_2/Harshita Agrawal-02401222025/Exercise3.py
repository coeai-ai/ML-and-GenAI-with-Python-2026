# Program to generate Fibonacci series up to n terms
i=0
j=1
count=2
n=int(input("Enter the number of Fibonacci terms to generate: "))

# Printing the first two terms of the series
print (i)
print (j)

# Generating Fibonacci series
while count<n:
    m=i+j
    print(m)
    i=j
    j=m
    count+=1
#swapping variables without using third variable
x=int(input("write first number- "))
y=int(input("write second number- "))

print("Before Swapping- ",x,y)

x=x+y
y=x-y
x=x-y

print("After Swapping- ", x , y)

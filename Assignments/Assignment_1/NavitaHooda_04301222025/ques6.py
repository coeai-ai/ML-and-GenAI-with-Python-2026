# swap 2 nos w/o third variable
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("The first number is", a, "and the second is", b)
a,b = b, a 
print("the swapped numbers are:" , a , "and", b)
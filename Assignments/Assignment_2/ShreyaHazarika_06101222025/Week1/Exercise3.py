# Determine how many terms to display
terms = int(input("Enter the number of terms for the Fibonacci series: "))

# Initialize the first two terms
n1, n2 = 0, 1
count = 0

print("Fibonacci Series:")
while count < terms:
    print(n1, end=" ")
    # Calculate the next term
    nth = n1 + n2
    # Update values for the next iteration
    n1 = n2
    n2 = nth
    count += 1
    print('\n') 

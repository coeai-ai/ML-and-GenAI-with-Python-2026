#print fibonacci series

n = int(input("enter the no till you want to print fabanacci :"))
# Initialize the list with the first two numbers
fib_series = [0, 1]

# Start the loop from 2 because we already have the first two elements
for i in range(2, n):
    next_element = fib_series[i - 1] + fib_series[i - 2]
    fib_series.append(next_element)

print("Fibonacci sequence:", fib_series)
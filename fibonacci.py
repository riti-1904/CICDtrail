def fibonacci_iterative(n):
    fib_series = [0, 1]
    for i in range(2, n):
        next_number = fib_series[-1] + fib_series[-2]
        fib_series.append(next_number)
    return fib_series[:n]

# Example usage
n = 10
print(fibonacci_iterative(n))

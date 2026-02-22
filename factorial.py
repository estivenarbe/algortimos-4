def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(15))

def fibonacci_simple(n):
    if n<= 1:
        return n
    return fibonacci_simple(n-1)+ fibonacci_simple(n-2)

print(fibonacci_simple(5))


def factorial(n):
    
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def combinations(n, m):
    
    return factorial(n) // (factorial(m) * factorial(n - m))

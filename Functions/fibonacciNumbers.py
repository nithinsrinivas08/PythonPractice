def fibonacci(n) :
    """Return the `n`th fibonacci number, for positive `n`."""
    if 0 <= n <= 1 :
        return n
    nMinus1, nMinus2 = 1,0
    result = None
    for f in range(n-1):
        result = nMinus2 + nMinus1
        nMinus2 = nMinus1
        nMinus1 = result
    
    return result

for i in range(36):
    print(i, fibonacci(i))
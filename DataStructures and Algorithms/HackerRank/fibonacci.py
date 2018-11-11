def fibonacci(n):
    n1 = 0
    n2 = 1
    fib = 0
    r = [n1]
    if n is 1:
        return r
    elif n < 1:
        return []
    else:
        r.append(n2)
        while n > 2:
            fib = n1 + n2
            n1 = n2
            n2 = fib
            r.append(fib)
            n -= 1
        return r


print(fibonacci(5))
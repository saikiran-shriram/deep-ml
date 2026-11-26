def first_n_fibonacci(n):
    # Return a list of the first n Fibonacci numbers
    result = []
    a = 0
    b = 1
    for i in range(n) :
        result.append(a)
        c = a + b
        a = b
        b = c
    return result
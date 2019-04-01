def fibonacci_modified(t1, t2, n):
    """
    Given terms t(i) and t(i+1) where i E (1, unlimited) t(i+2) is computed
    using the following relation:
    t(i+2) = t(i) + t(i+1) ^ 2
    .. doctests::
       >>> fibonacci_modified(0, 1, 5)
       5
    """
    fib_sequences = [0] * n
    fib_sequences[0] = t1
    fib_sequences[1] = t2
    for i in range(2, n):
        fib_sequences[i] = fib_sequences[i-2] + fib_sequences[i-1] ** 2
    return fib_sequences[n-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()

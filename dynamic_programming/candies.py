
def candies(n, arr):
    """
    .. doctest::
       >>> candies(3, [1, 2, 2])
       4
       >>> candies(10, [2, 4, 2, 6, 1, 7, 8, 9, 2, 1])
       19
       >>> candies(8, [2, 4, 3, 5, 2, 6, 4, 5])
       12
    """
    dp = [1] * n
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            dp[i] += dp[i- 1]
    for i in range(n -2, -1, -1):
        if arr[i] > arr[i + 1] and dp[i] <= dp[i + 1]:
            dp[i] = dp[i + 1] + 1
    return sum(dp)



if __name__ == '__main__':
    import doctest
    doctest.testmod()

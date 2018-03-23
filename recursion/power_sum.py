import sys

def powerSum(X, N, c=1):
    """X=10 N=2 result=1 10=1**2 + 3**2"""
    v = c ** N
    if v > X:
        return 0
    elif v == X:
        return 1
    return powerSum(X, N, c + 1) + powerSum(X - v, N, c + 1)

if __name__ == '__main__':
    X = int(raw_input().strip())
    N = int(raw_input().strip())
    result = powerSum(X, N)
    print result

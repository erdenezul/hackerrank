for _ in xrange(input()):
    A = []
    ans = "YES"
    n = input()
    for i in xrange(n):
        A.append(raw_input().strip())
    for i in xrange(n - 1):
        #x, y = ????
        x, y = sorted(A[i]), sorted(A[i+1])
        for j in xrange(n):
            if x[j] > y[j]:
                ans = "NO"
    print ans

# Enter your code here. Read input from STDIN. Print output to STDOUT

dire = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def dfs(i, j, mat, mark, color):
    if i < 0 or i >= len(mat) or j < 0 or j >= len(mat[0]):
        return
    if mat[i][j] == 0:
        return
    if mark[i][j] != -1:
        return
    mark[i][j] = color
    for d in dire:
        dfs(i + d[0], j + d[1], mat, mark, c)

N = int(raw_input())
M = int(raw_input())
mat = []
for i in xrange(N):
    mat.append(map(int, raw_input().split()))
mark = [[-1] * M for i in xrange(N)]
c = 0
for i in xrange(N):
    for j in xrange(M):
        dfs(i, j, mat, mark, c)
        c += 1

count = [0] * (N * M)
for i in xrange(N):
    for j in xrange(M):
        if mark[i][j] != -1:
            count[mark[i][j]] += 1
print max(count)

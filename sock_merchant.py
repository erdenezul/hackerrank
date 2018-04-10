import sys

def sock_merchant(n, arr):
    number_map = {}
    for num in arr:
        number_map[num] = number_map.get(num, 0) + 1
    count = 0
    for value in number_map.values():
        count += value / 2
    return count

n  = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
result = sock_merchant(n, arr)
print result

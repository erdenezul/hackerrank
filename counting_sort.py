#!/bin/python

import sys


def countingSort(arr):
    # Complete this function
    result = [0] * (n + 1)
    newarr = []
    for num in arr:
        result[num] += 1
    for i, value in enumerate(result):
        newarr.extend([i] * value)
    return newarr

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    result = countingSort(arr)
    print " ".join(map(str, result))




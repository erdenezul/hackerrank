#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(a):
    previous_sum = 0
    for i in range(4):
        for j in range(4):
            t_sum = a[i][j] + a[i][j + 1] + a[i][j + 2] + \
                    a[i + 1][j + 1] + \
                    a[i + 2][j] + a[i + 2][j + 1] + a[i + 2][j + 2]
            if previous_sum < t_sum:
                previous_sum = t_sum
    return previous_sum


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, raw_input().rstrip().split())))

    result = hourglassSum(arr)

    #fptr.write(str(result) + '\n')

    #fptr.close()
    print(result)

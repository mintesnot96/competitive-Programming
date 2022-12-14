#!/bin/python3

import math
import os
import random
import re
import sys
def countingSort(arr):
    # Write your code here
    result = []
    for i in range(100):
        result.append(0)
    for i in range(len(arr)):
        result[arr[i]] = result[arr[i]]+1
    # print(*arr)
    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys
def countingValleys(steps, path):
    # Write your code here
    count=0
    sealevel=0
    for i in range(steps):
        if path[i]=="U":
            sealevel+=1
        if path[i]=="D":
            sealevel-=1
        if sealevel==0 and path[i]=="U":
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

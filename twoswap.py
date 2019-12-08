#You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] 
#without any duplicates. You are allowed to swap any two elements. 
#You need to find the minimum number of swaps required to sort the array in ascending order.


#CODE


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps=0
    temp = [0] * (len(arr) + 1)
    for pos, val in enumerate(arr):
        temp[val] = pos
        pos += 1
    for i in range(len(arr)):
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            arr[temp[i+1]] = t
            temp[t] = temp[i+1]
        
    return(swaps)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()


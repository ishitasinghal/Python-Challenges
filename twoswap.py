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
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if(arr[j]>arr[j+1]):
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                swaps=swaps+1
    return(swaps)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

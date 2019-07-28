#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    a = 0
    x = True
    for i in range(6):
        #arr.append(list(input().split())[:6])
        n = len(arr[i])
        while n < 6 :
            arr[i].append("0")
            n = n + 1
    for i in range(4) :
        for j in range(4) :
            s = int(arr[i][j]) + int(arr[i][j+1]) + int(arr[i][j+2]) + int(arr[i+1][j+1]) +             int(arr[i+2][j]) + int(arr[i+2][j+1]) + int(arr[i+2][j+2])
            if x :
                a = s
                x = False
            if s > a :
                a = s
    print(a)

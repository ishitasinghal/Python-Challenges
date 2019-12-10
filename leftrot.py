def rotLeft(a, d):
    while(d>0):
        temp = a[0]
        for i in range(0,len(a)-1):
            a[i]=a[i+1]
        a[len(a)-1]=temp
        # print(a)
        d=d-1
    print(a)
        

a = [1,2,3,4,5]
d=2
rotLeft(a,d)



#Actual code

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    while(d>0):
        temp = a[0]
        for i in range(0,len(a)-1):
            a[i]=a[i+1]
        a[len(a)-1]=temp
        d=d-1
    return(a)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

#Handle the chaotic queue
#Any person in the queue can bribe the person directly in front of them to swap positions. 
#If two people swap positions, they still wear the same sticker denoting their original places in line. 
#One person can bribe at most two others. 
#decide you must know the minimum number of bribes that took place to get the queue into its current state!

#Link to the complete problem statement-
#https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

#CODE

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    flist=[]
    nq = sort(q)
    for i in range(len(q)):
        flist.append(nq[i]-q[i])
    print(flist)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

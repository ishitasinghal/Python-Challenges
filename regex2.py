# Problem Statement:
# ou are given a string S.
# Your task is to find the indices of the start and end of k string in S .

import re

s = input()
k = input()
index = 0

if re.search(k, s):
    while index+len(k) < len(s):
        m = re.search(k, s[index:]) 
        
        print("({0}, {1})".format(index+m.start(), index+m.end()-1)) 
        
        index += m.start() 
else:
    print((-1, -1))

# Problem Statement:
# ou are given a string S.
# Your task is to find the indices of the start and end of k string in S .

S = input()
k = input()
import re
pattern = re.compile(k)
r = pattern.search(S)
if not r: 
    print("(-1, -1)")
while r:
    print("({0}, {1})".format(r.start(), r.end() - 1))
    r = pattern.search(S,r.start() + 1)

# Source: "https://codeforces.com/problemset/problem/1335/B"

# Problem Statement:
# You are given three positive integers n, a and b. You have to construct a 
# string s of length n consisting of lowercase Latin letters such that each 
# substring of length a has exactly b distinct letters.

# CODE:

#Solution 1

import random
import string
n, a, b = input().split()
string1 = ""
while(len(string1)<int(b)):
    string1 = string1 + (random.choice(string.ascii_lowercase))
for i in range(int(a)-int(b)):
    string1=string1+string1[i]

for i in range(int(n)-int(a)):
    string1=string1+string1[i]

print(string1)

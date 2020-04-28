# Source: "https://codeforces.com/problemset/problem/1335/B"

# Problem Statement:
# You are given three positive integers n, a and b. You have to construct a 
# string s of length n consisting of lowercase Latin letters such that each 
# substring of length a has exactly b distinct letters.

# CODE:

import random
import string
n, a, b = input().split()
string1 = ""
while(len(string1)<int(a)):
    string1 = string1 + (random.choice(string.ascii_letters))
# print(string1)
res = [string1[i: j] for i in range(len(string1)) for j in range(i + 1, len(string1) + 1) if len(string1[i:j]) == int(b)]
print(res)

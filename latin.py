Source: "https://codeforces.com/problemset/problem/1335/B"

Problem Statement:
You are given three positive integers n, a and b. You have to construct a 
string s of length n consisting of lowercase Latin letters such that each 
substring of length a has exactly b distinct letters.

CODE:

import random
import string
n, a, b = input().split()
print(random.choice(string.ascii_letters))

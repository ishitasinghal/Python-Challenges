# Problem Statement
# Write a function solution that :
# Given a string S of length N, returns the length of the shortest unique
# substring of S, i.e. the length of the shortest word, which ocuurs in S exactly once. 
# Example:
# 1. Given S = "abaaba" the function should return 2. The shortest unique substring of S is aa.
# 2. Given S="zyzyzyz" the function should return 5. he shortest unique substring of S is "yzyzy"

# Note that there are shortest words, like yzy, occurences of which overlap 
# but they still count as mulitple occurences.

# 3. Given S = "aabbbabaaa" the func should return 3. all substring of size ocuurs in S 
# atleast twice.

# CODE

st = "abaaba"
stlist = [st[i: j] for i in range(len(st)) for j in range(i + 1, len(st) + 1)]
print(stlist)

from itertools import permutations
dict1 = { 1:['a','b','c'],
          2:['d','e','f'],
          3:['g','h','i'],
          4:['j','k','l'],
          5:['m','n','o'],
          6:['p','q','r'],
          7:['s','t','u'],
          8:['v','w','x'],
          9:['y','z']
          }
n = input()
nlist = []
for i in n:
    nlist.extend(dict1[int(i)])
print(nlist)

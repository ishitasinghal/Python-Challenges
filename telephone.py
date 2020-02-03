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
result = [(x,y) for x in dict1[1] for y in dict1[2]]
print(result)

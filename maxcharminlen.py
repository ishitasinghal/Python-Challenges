sample = 'abcda'
subs = [sample[i: j] for i in range(len(sample)) for j in range(i + 1, len(sample) + 1)] 
max_dist = len(set(sample))
print(max_dist)

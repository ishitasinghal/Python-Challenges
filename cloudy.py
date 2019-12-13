def jumpingOnClouds(c):
    jumps=0
    steps=0
    while steps<len(c)-1:
        if steps+2<len(c) and c[steps+2]!=1 :
            steps+=1
        steps+=1
        jumps+=1
    return jumps
    
c=[0,0,0,0,1,0]
print(jumpingOnClouds(c))

def jumpingOnClouds(c):
    safepath = [i for i in range(len(c)) if(c[i]==0)]
    possible=[]
    for i in safepath:
        if(i+2 in safepath):
            possible.append(i)
            possible.append(i+2)
            i=i+2
        else:
            possible.append(i)
            possible.append(i+1)
            i=i+1
            
    return(possible)
c=[0,0,0,0,1,0]
print(jumpingOnClouds(c))

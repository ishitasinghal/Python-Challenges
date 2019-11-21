def beautifulQuadruples(a, b, c, d):
    quadruples=0
    for i in range(1,a+1):
        for j in range(1,b+1):
            for k in range(1,c+1):
                for l in range(1,d+1):
                    if i^j^k^l!=0 and i<=j<=k<=l :
                        quadruples=quadruples+1
    return(quadruples)

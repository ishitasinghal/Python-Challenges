safepath = [i for i in range(len(c)) if(c[i]==0)]
    possible=[safepath[0]]
    step=0
    while(step!=len(safepath)):
        if(safepath[step]+2 in safepath):
            possible.append(safepath[step]+2)
            step=step+2
        elif(safepath[step]+1 in safepath):
            possible.append(safepath[step]+1)
            step=step+1
    return(len(possible))

c = [0, 0, 0, 1, 0, 0]
safepath = [i for i in range(len(c)) if(c[i]==0)] #making a list of the possible safepaths
possible = [safepath[j] for j in range(len(safepath)-1) if(safepath[j+1]-safepath[j])<=2]
p2=[]
for i in range(len(possible)):
    if(possible[i+2]-possible[i]==2):
        p2.append
print(safepath)

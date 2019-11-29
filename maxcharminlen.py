NO_OF_CHARS = 256
def dischar(str,n):
    count[0]*NO_OF_CHARS
    for i in range(n):
        count[ord(str[i])]+=1
    maxd=0
    for j in range(NO_OF_CHARS):
        if(count[i]!=0):
                 maxd+=1
    return maxd

def subs(str):
    n=len(str)
    maxdis=dischar(str,n)
    minl=n
    for i in range(n):
        for j in range(n):
           subs=str[i:j]
           subs_length=len(subs)
           sub_dist_char=max_distinct_char(subs,subs_length)
           if(subs_length<minl and max_distinct==sub_dist_char):
                minl=subslength
    return minl
str="abcda"
l=subs(str)
print(l)

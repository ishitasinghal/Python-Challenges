def rotLeft(a, d):
    while(d>0):
        a[len(a)-1]=a[0]
        for i in range(0,len(a)-1):
            a[i]=a[i+1]
            print(a)
        d=d-1

a = [1,2,3,4,5]
d=2
rotLeft(a,d)


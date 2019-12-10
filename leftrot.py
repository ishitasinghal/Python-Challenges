def rotLeft(a, d):
    while(d>0):
        temp = a[0]
        for i in range(0,len(a)-1):
            a[i]=a[i+1]
        a[len(a)-1]=temp
        # print(a)
        d=d-1
    print(a)
        

a = [1,2,3,4,5]
d=2
rotLeft(a,d)

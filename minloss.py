def minimumLoss(price):
    list1 =[]
    j=0
    i=0
    while(i<=len(price)):
        for j in range(len(price)-1):
            
            list1.append(price[j]-price[j+1])
            
            j=j+1
            #print(list1)
        i=i+1
        price=price[i:]
        list2=list1
    #print(len(list2))    
    list2 = [x for x in list2 if x >= 0 ]
    print(min(list2))

price=[20,7,8,2,5]
minimumLoss(price)



def minimumLoss(price):
    list1 =[]
    j=0
    i=0
    while(i<=len(price)):
        for j in range(len(price)-1):
            for k in range(j+1,len(price)):
                list1.append(price[j]-price[k])
            j=j+1
            #print(list1)
        i=i+1
        price=price[i:]
        list2=list1
    #print(len(list2))    
    list2 = [x for x in list2 if x >= 0 ]
    return(min(list2))

#You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] 
#without any duplicates. You are allowed to swap any two elements. 
#You need to find the minimum number of swaps required to sort the array in ascending order.
ef Repeat(x): 

    _size = len(x) 

    repeated = [] 

    for i in range(_size): 

        k = i + 1

        for j in range(k, _size): 

            if x[i] == x[j] and x[i] not in repeated: 

                repeated.append(x[i]) 

    return repeated 

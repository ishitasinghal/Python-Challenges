#Practice part 1
#Input1 : 5 12
#Input2 : 1 2 3 7 5
#Output : 2 4
#
Logic : sum of elements from 2nd position to 4th position is 12

def sumlist(arr, n, m):
    for i in range(n):
        currentsum = arr[i]
        j=i+1
        while(j<=n):
            if(currentsum==m):
                print(i,j-1)
                return 1

            if(currentsum>m or j==n):
                break;
            currentsum=currentsum+arr[j];
            j=j+1

    print("-1")
    return 0
n,m = input().split()
n=int(n)
m=int(m)
arr=list(map(int,input().split()))
sumlist(arr,n,m)

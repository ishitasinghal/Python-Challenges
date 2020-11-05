"https://www.hackerrank.com/challenges/ctci-merge-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting"

#CODE
def countInversions(arr):
    count=0
    dummy=[arr[0]]
    for i in range(1,len(arr)):
        index=bisect.bisect_right(dummy,arr[i])
        count+=(i-index)
        dummy.insert(index,arr[i])
    return count

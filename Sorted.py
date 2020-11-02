#this basic program uses the sorted built-in facility in python.
#Problrm statement
#Print the N lines of the sorted table. Each line should contain the space separated elements.
#Check out the given link further :
#https://www.hackerrank.com/challenges/python-sort-sort/problem

#Code

def athlete(arr, q):
    arr1 = sorted(arr,key=lambda x: x[q])
    for i in arr1:
        print(*i)

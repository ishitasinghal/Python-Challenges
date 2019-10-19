#making use of the zipped iterable function in Python.
#Question:
#Print the averages of all students on separate lines.
#The averages must be correct up to 1 decimal place.
#Input Format
#The first line contains N and X separated by a space.
#The next X lines contains the space separated marks obtained by students in a particular subject.

#Code 
n, x = map(int, input().split())
res = []
for _ in range(x):
    res.append( map(float, input().split())) 
for i in zip(*res): 
    print( sum(i)/len(i) )
    


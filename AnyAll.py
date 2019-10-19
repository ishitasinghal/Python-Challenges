#this basic code makes use of the python's built-in any() and all() function.
#Problem statement
#Given a space separated list of integers. 
#If all the integers are positive, then check if any integer is a palindromic integer.
#Condition 1:
#All the integers in the list are positive.
#Condition 2: any integer is a palindromic integer.

#Code

n,nl = int(input()),input().split()
print(all([int(i)>0 for i in nl]) and any([j == j[::-1] for j in nl]))

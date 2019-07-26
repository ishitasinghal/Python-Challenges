import re
list1 = []
num = int(input("Enter number of inputs"))
for i in range(num):
    firstNameEmailID = input().split()
    firstName = firstNameEmailID[0]
    emailID = firstNameEmailID[1]
    find = re.search("[@][a-z]+", emailID).group(0)
    s = find.split('@')
    if(s[1]=='gmail'):
         list1.append(firstName)
list1.sort()
for j in list1:
    print(j)
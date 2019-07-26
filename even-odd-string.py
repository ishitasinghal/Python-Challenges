# t = int(input("Enter number of test cases"))
# for i in range(t):
#     string = input()
# print(string)

# for i in range(int(input())):
#     s=input()
# print(*["".join(s[::2]),"".join(s[1::2])])

# for i in range(int(input())):
#     s = input()
#     print(s[::2], s[1::2])

# arr = [1,4,2,7,5,9,2]
# list1=[]
# for i in range(len(arr)-1,-1, -1):
#     list1.append(arr[i])
# print(list1)

#############################################################################################################################################

# dict1 = {
# 'sam' :99912222,
# 'tom' :11122222,
# 'harry' : 12299933
# }

n = int(input())          #n is the number of items you want to enter
dict1 ={}
for i in range(n):
    text = input().split()     #split the input text based on space & store in the list 'text'
    dict1[text[0]] = text[1]       #assign the 1st item to key and 2nd item to value of the dictionary
print(dict1)
#print(dict1)
try:
    while True:
        find = input("Enter the element u wanna find")
        if find != "":
            if (find in dict1.keys()):
                print(find, "=", dict1[find])
            else:
                print("Not found")
        else:
            break
except EOFError:
    pass





                # Stuff to be done



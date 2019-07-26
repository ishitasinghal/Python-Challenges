# def fact(x):
#     f=1
#     if(x<=1):
#         return 1
#     else:
#         f=x*fact(x-1)
#         return f
#
# num = int(input("Enter number"))
# factorial = fact(num)
# print(factorial)

# n = int(input("Enter number"))
# list1 = []
# while(n!=1):
#     list1.append(int(n%2))
#     n=int(n/2)
# list1.append(1)
# print(list1)

##########CONVERTING TO BINARY##########################


def maxRepeating(binary):
    n = len(binary)
    count = 0
    #res = binary[0]
    cur_count = 1
    for i in range(n):
        if (i < n-1 and binary[i] == binary[i + 1]):
            cur_count += 1

        else:
            if cur_count > count:
                count = cur_count
                #res = binary[i]
            cur_count = 1
    return count

n = int(input("Enter number"))
binary = bin(n).replace("0b","")
count=0
# for i in binary:
#     if((i==1) and (i+1)==1):
#         count = count+1
counting=maxRepeating(binary)
print(counting)


# print("Enter your budget, number of models of keyboard, and number of models of USB")
# list1 = [int(input(x)) for x in range(3)]
# # print(list1[1])
# list2 = []

list1 = [60, 2, 3]
list2 = [30, 50]
list3 = [10, 5, 8]

for i in list2:
    for j in list3:
        if((i+j)<=list1[0]):
            list4 = list((i,j))
print(list4)
ar=[10, 20, 20, 10, 10, 30, 50, 10, 20]
my_dict = {i:ar.count(i) for i in ar}
my_list=[]
a=b=c=0
for value in my_dict:
    my_list.append(my_dict[value])
for i in my_list:
    if(i%2==1):
        a=a+int(i/2)
    elif(i%2==0):
        b=b+int(i/2)
    elif(i==1):
        c=0
count = a+b+c
print(count)

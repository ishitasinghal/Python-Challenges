string = "a"
# count=0
# num = int(input("How many characters u wanna print"))
# i=1
# sub=string
# while(len(sub)<=num):
#     sub = string*i
#     i=i+1
# #print(sub)
# new_sub=sub[0:num]
# #print(new_sub)
# for i in new_sub:
#     if(i=='a'):
#         count=count+1
# print(count)

s, n = input().strip(), int(input().strip())
print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))
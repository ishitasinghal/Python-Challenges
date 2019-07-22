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

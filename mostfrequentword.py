string = "This is a string from which words are to be counted is a this from words words counted"
list1 = string.split()
fre = []
for i in list1:
    fre.append(list1.count(i))
print(dict(list(zip(list1, fre))))

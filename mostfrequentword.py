
##list1 = string.split()
##fre = []
##for i in list1:
##    fre.append(list1.count(i))
##print(dict(list(zip(list1, fre))))




###########Solution#############
from collections import Counter
string = "This is a string from which words are to be counted is a this from words words counted"
list1 = string.split()
countstr = Counter(list1)
##print(countstr.most_common(1)[0])
res_list = [x for x,_ in countstr.most_common(1)]
print(res_list[0])

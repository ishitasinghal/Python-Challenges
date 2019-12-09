#Given two strings a, and b, that may or may not be of the same length, determine 
#the minimum number of character deletions required to make  and  anagrams. 
#Any characters can be deleted from either of the strings.
#we can delete from string and from string  
#so that both remaining strings are which are anagrams.

#Code

s1 = "fcrxzwscanmligyxyvym"
s2 = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"
ns=""
for i in s1:
    if(i in s2):
        ns = ns+i
nlen = len(ns)
final = (len(s1)-len(ns)+len(s2)-len(ns))
print(final)







def check(s1, s2): 

      

    # the sorted strings are checked  

    if(sorted(s1)== sorted(s2)): 

        print("The strings are anagrams.")  

    else: 

        print("The strings aren't anagrams.")          

          

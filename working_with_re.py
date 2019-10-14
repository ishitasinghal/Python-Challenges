import re
for _ in range(int(input())):
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))
    #a basic working with re(regular expression) of python module.
    
    #Input 
    # first line number of test cases
    #4
#4.0O0
#-1.00
#+4.54
#SomeRandomStuff
#Check for all possible floating expressions
#requirements for a number to be considered as floating.

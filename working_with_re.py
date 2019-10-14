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
# Number can start with +, - or . symbol.
#For example:
#✔ +4.50
#✔-1.0
#✔.5
#✔-.7
#✔+.4
#✖-+4.5
#Number must contain at least  decimal value.
#For example:
#✖ 12.
#✔12.0  
 #Number must have exactly one . symbol.
 #Number must not give any exceptions when converted using float(n).

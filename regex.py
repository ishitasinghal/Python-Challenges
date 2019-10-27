#Problem Statement
#Given a string consisting only of digits 0-9, commas ,, and dots .
#split it !

#CODE

regex_pattern = r",|\."	

import re
print("\n".join(re.split(regex_pattern, input())))

#https://www.hackerrank.com/challenges/re-split/problem

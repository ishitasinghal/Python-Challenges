#This program shows the built-in function in python.
#The reduce() function applies a function of two arguments
#cumulatively on a list of objects in succession from left 
#to right to reduce it to one value. 

#Code
from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda a,b: a*b,fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)

    #https://www.hackerrank.com/challenges/reduce-function/problem
    #link to details.

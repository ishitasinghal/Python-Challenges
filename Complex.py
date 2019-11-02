#Problem statement

#One line of input: The real and imaginary part of a number separated by a space.
#Output: Print the result of their addition, subtraction, multiplication, division and modulus operations.

import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real,self.imaginary=real,imaginary
    def __add__(self, no):
        temp=Complex(0,0)
        temp.real,temp.imaginary=self.real+no.real,self.imaginary+no.imaginary
        return temp
    def __sub__(self, no):
        temp=Complex(0,0)
        temp.real,temp.imaginary=self.real-no.real,self.imaginary-no.imaginary
        return temp
    def __mul__(self, no):
        temp=Complex(0,0)
        temp.real,temp.imaginary=(self.real*no.real-self.imaginary*no.imaginary),(self.real*no.imaginary+self.imaginary*no.real)
        return temp
    def __truediv__(self, no):
        temp=Complex(0,0)
        temp.real,temp.imaginary=(self.real*no.real+self.imaginary*no.imaginary)/(no.real**2+no.imaginary**2),(self.imaginary*no.real-self.real*no.imaginary)/(no.real**2+no.imaginary**2)
        return temp
    def mod(self):
        temp=Complex(0,0)
        temp.real,temp.imaginary=math.sqrt(self.real**2+self.imaginary**2),0
        return temp
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')

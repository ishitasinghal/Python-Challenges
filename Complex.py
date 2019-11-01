#Problem statement

#One line of input: The real and imaginary part of a number separated by a space.
#Output: Print the result of their addition, subtraction, multiplication, division and modulus operations.

class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary = imaginary
        
    def __add__(self, no):
        return(complex(self.real+no.real, self.imaginary+no.imaginary))
        
    def __sub__(self, no):
        return(complex(self.real-no.real, self.imaginary-no.imaginary))
        
    def __mul__(self, no):
        return complex(self.real*no.real-self.imaginary*no.imaginary, self.real*no.imaginary+self.imaginary*no.real)

    def __truediv__(self, no):
        try: 
            return self.__mul__(complex(no.real, -1*no.imaginary)).__mul__(complex(1.0/(no.mod().real)**2, 0))
        except ZeroDivisionError as e:
            print(e)
            return None

    def mod(self):
        return complex(pow(self.real**2+self.imaginary**2, 0.5), 0)

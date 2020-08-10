import random
import decimal
from decimal import Decimal

g_ctx = decimal.getcontext()
g_ctx.prec = 10
g_ctx.rounding = decimal.ROUND_HALF_EVEN

class Qualean:
    def __init__(self, real):
        self.qual = self.generate_qual(real)

    def generate_qual(self, real):
        if not (real in [-1, 0, 1]):
            raise ValueError("Real values can only accept -1,0 or 1")
        else:
            y = real * random.uniform(-1, 1)
            x = Decimal(y)
            return round(x, 10)

    def __and__(self, value):
        if(not(self.qual)):
            return False
        if(not(isinstance(value, Qualean))):
            raise ValueError("Argument not defined")
        else :
            return bool(self.qual) and bool(value.qual)
 
    def __or__(self, value):
        if(self.qual):
            return True
        if(not(isinstance(value, Qualean))):
            raise ValueError("Argument not defined")
        else :
            return bool(self.qual) or bool(value.qual)

    def __repr__(self):
        return 'Qualean number in decimal representation is {}'.format(self.qual) 

    def __str__(self):
        return 'Qualean number is {}'.format(self.qual) 

    def __add__(self, value):
        if isinstance(value, Qualean):
            return self.qual + value.qual
        raise NotImplementedError

    def __eq__(self, value):
        if isinstance(value, Qualean):
            return self.qual == value.qual
        raise NotImplementedError

    def __float__(self):
        return float(self.qual)

    def __gt__(self, value):
        if isinstance(value, Qualean):
            return self.qual > value.qual
        raise NotImplementedError

    def __ge__(self, value):
        if isinstance(value, Qualean):
            return self.qual >= value.qual
        raise NotImplementedError

    def __invertsign__(self):
        return self.qual * -1

    def __le__(self, value):
        if isinstance(value, Qualean):
            return self.qual <= value.qual
        raise NotImplementedError

    def __lt__(self, value):
        if isinstance(value, Qualean):
            return self.qual < value.qual
        raise NotImplementedError

    def __mul__(self, value):
        if isinstance(value, Qualean):
            return self.qual * value.qual
        raise NotImplementedError

    def __sqrt__(self):
        if self.qual < 0:
            num_sqrt = Decimal.sqrt(self.__invertsign__())  # cmath.sqrt(self.qual) this can also be used 
            return complex(0, round(num_sqrt,10))
        else:
            num_sqrt = Decimal.sqrt(self.qual)
            return complex(round(num_sqrt,10), 0)

    def __bool__(self):
        return (self.qual != 0)



class Fraction(object):
    def __init__(self,num,denom):
        assert type(num) == int and type(denom) == int
        self.num=num
        self.denom= denom
    def __str__(self):
        return str(self.num) + "/" + str(self.denom)
    def __add__(self,other):
        top= self.num*other.denom + other.num*self.denom
        bott=self.denom *other.denom
        return Fraction(top,bott)
    def __float__(self):
        return self.num / self.denom
    def inverse(self):
        return Fraction(self.denom,self.num)
    def __mul__(self,other):
        top= self.num*other.num
        bott=self.denom *other.denom
        return Fraction(top,bott)

a=Fraction(4,5)
b=Fraction(5,6)
c=a+b
print(c)
print(float(c))
print(Fraction.__float__(c))
print(Fraction.inverse(a))
print(Fraction.__float__(c.inverse()))
print(a*b)

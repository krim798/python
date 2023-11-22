class fraction(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator=denominator
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)
    def getNumer(self):
        return self.numerator
    def getDenom(self):
        return self.denominator
    def __add__(self,other):
        newnum= self.getNumer()*other.getDenom() + other.getNumer()*self.getDenom()
        newden=(self.getDenom()*other.getDenom())
        return fraction(newnum,newden)
    def __sub__(self,other):
        newnum= self.numerator * other.denominator - other.numerator * self.denominator
        newden=(self.denominator * other.denominator)
        return fraction(newnum,newden)
    def convert(self):
        return self.getNumer()/self.getDenom()

f=fraction(5,6)
g=fraction(10,12)
print(f)
print(f.getNumer())
print(f+g)
print(g-f)
print(f.convert())
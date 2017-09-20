

class Fraction(object):
    def __init__(self,numerator,denominator=1):
        self.numerator = numerator
        self.denominator = denominator
    def __str__(self):
        """
        print presentation with numerator/denominator
        
        """
        
        return str(self.numerator) + '/' + str(self.denominator)
    def __add__(self, other):
        """
        add two fraction
        
        """
        return Fraction( (self.numerator * other.denominator + 
                          self.denominator * other.numerator) ,
                       (self.denominator * other.denominator) ).simplify()
    def invert(self):
        """
        invert a fraction
        
        """
        return Fraction(self.denominator, self.numerator)
    def to_float(self):
        """
        decimal representation of a fraction
        
        """
        return float(self.numerator) / float(self.denominator)
    def integer(self):
        """
        return integer part of a fraction
        """
        return int( self.numerator / self.denominator )
    def __sub__(self, other):
        """
        subtract fraction
        """
        return Fraction( (self.numerator * other.denominator
                          - self.denominator * other.numerator)
                       , (self.denominator * other.denominator) )
    def __mul__(self, other):
        """
        multiply fraction
        """
        return Fraction( (self.numerator * other.numerator) , 
                        (self.denominator * other.denominator))
    def __div__(self, other):
        """
        divide fraction
        """
        return Fraction(Fraction.__mul__( self , Fraction.invert(other)))
    def simplify(self):
        
        """
        simplify a fraction
        """
        from fractions import gcd        
        c=gcd(self.numerator, self.denominator)
        d= self.numerator/c
        e= self.denominator/c
        return Fraction(d, e)

    
    def __eq__(self, other):
        """
        equal fractions        
        """
        k=Fraction.__sub__(self, other)
        if k.numerator == 0:
            return '{} and {} are equal'.format(self, other)
        else:
            return '{} and {} are not equal'.format(self, other)





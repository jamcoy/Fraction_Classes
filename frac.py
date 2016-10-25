from fractions import gcd


class Fraction(object):
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator

    def __repr__(self):
        if self.num >= self.den:
            qd = divmod(self.num, self.den)
            whole_number = qd[0]
            remaining_num = qd[1]
            remaining_den = self.den
            if qd[1] == 0:
                return 'Vulgar fraction equates to: %s' % whole_number
            else:
                return 'Vulgar fraction equates to: %s %s/%s' % (whole_number, remaining_num, remaining_den)
        else:
            divisor = gcd(self.num, self.den)
            smallest_num = self.num / divisor
            smallest_den = self.den / divisor
            return '%s/%s' % (smallest_num, smallest_den)

    def __add__(self, other):
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)

    def __div__(self, other):
        return Fraction(self.num * other.den, self.den * other.num)


f1 = Fraction(3, 2)
f2 = Fraction(1, 4)
print "f1 = 3/2"
print "f2 = 1/4"
print

print "f1 + f2"
f3 = f1 + f2
print f3
print

print "f1 / f2"
f3 = f1 / f2
print f3
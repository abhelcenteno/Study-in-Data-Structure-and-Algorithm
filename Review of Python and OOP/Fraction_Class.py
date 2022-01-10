def gcd(num1, num2):
    while num1 % num2 != 0:
        num1, num2 = num2, num1 % num2
    return num2


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __sub__(self, other_fraction):
        new_num = self.num * other_fraction.den - self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __mul__(self, other_fraction):
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __truediv__(self, other_fraction):
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __str__(self):
        if self.num == self.den or self.den == 1:
            return str(self.num)
        elif self.num == 0:
            return str(0)
        return f'{self.num}/{self.den}'
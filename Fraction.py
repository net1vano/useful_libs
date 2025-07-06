class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ZeroDivisionError("Знаменатель не может быть равен нулю")
        self.numerator = numerator
        self.denominator = denominator

        _gcd = Fraction._gcd(self.numerator, self.denominator)
        self.numerator //= _gcd
        self.denominator //= _gcd

        if self.denominator < 0:
            self.denominator *= -1
            self.numerator *= -1


    @staticmethod
    def _gcd(a: int, b: int):
        a, b = abs(a), abs(b)
        while b != 0:
            a, b = b, a % b
        return a

    def reduce(self):
        _gcd = Fraction._gcd(self.numerator, self.denominator)
        self.numerator //= _gcd
        self.denominator //= _gcd
        if self.denominator < 0:
            self.denominator *= -1
            self.numerator *= -1

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return Fraction(
            numerator=(self.numerator * other.denominator) + (other.numerator * self.denominator),
            denominator=self.denominator * other.denominator)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return Fraction(
            numerator=(self.numerator * other.denominator) - (other.numerator * self.denominator),
            denominator=self.denominator * other.denominator)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return Fraction(
            numerator=self.numerator * other.numerator,
            denominator=self.denominator * other.denominator)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return Fraction(
            numerator=self.numerator * other.denominator,
            denominator=self.denominator * other.numerator)

    def __eq__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __lt__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return self.numerator * other.denominator <= other.numerator * self.denominator
    def __gt__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return self.numerator * other.denominator > other.numerator * self.denominator
    def __ge__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return self.numerator * other.denominator >= other.numerator * self.denominator
    def __repr__(self):
        return f'<{self.numerator}/{self.denominator}>'

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return Fraction(other, 1) - self

    def __rmul__(self, other):
        return self * other

    def __rtruediv__(self, other):
        return Fraction(other, 1) / self


fr1 = Fraction(2, 4)
fr2 = Fraction(2, 5)
fr3 = fr1 * fr2
print(fr1 <= fr2)
print(fr3)
import math


class Rational:
    """
        Class that works with fractions
    """
    def __init__(self, *args, **kwargs):
        a = b = None
        if len(args) == 1 and isinstance(args[0], str):
            a, b = map(int, args[0].split("/"))
            if b == "0":
                raise ValueError("Denominator is zero")
        elif len(kwargs) == 2:
            if not isinstance(kwargs["numerator"], int) or not isinstance(kwargs["denominator"], int):
                raise TypeError("Invalid type, should be integer")
            if kwargs["denominator"] == 0:
                raise ValueError("Denominator is zero")
            a, b = kwargs.values()
        else:
            raise Exception("Invalid Input")
        self.__numerator, self.__denominator = Rational.__make_it_shorter(a, b)

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return  self.__denominator

    @staticmethod
    def __make_it_shorter(*args):
        """
            method that returns shorten version of numerator and denominator
        :param args: list of fraction's part
        """
        gcd = math.gcd(args[0], args[1])
        numerator = args[0] // gcd
        denominator = args[1] // gcd
        return numerator, denominator

    def __add__(self, other):
        if isinstance(other, Rational):
            return Rational(numerator=self.numerator* other.denominator + other.numerator,
                            denominator=self.numerator*other.denominator)
        if isinstance(other, int):
            return Rational(numerator= self.numerator + self.denominator* other, denominator=self.denominator)
        raise TypeError

    def __sub__(self, other):
        if isinstance(other, Rational):
            return Rational(numerator=self.numerator * other.denominator - other.numerator,
                            denominator=self.denominator* other.denominator)
        if isinstance(other, int):
            return Rational(numerator= self.numerator - self.denominator* other, denominator=self.denominator)
        raise TypeError

    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(numerator=self.numerator*other.numerator,
                            denominator=self.denominator*other.denominator)
        if isinstance(other, int):
            return Rational(numerator=self.numerator*other, denominator=self.denominator)
        raise TypeError

    def __truediv__(self, other):
        if isinstance(other, Rational):
            first_num = self.numerator / self.denominator
            second_num = other.numerator / other.denominator
            return Rational(numerator= self.numerator * other.denominator,
                            denominator=self.denominator*other.numerator)
        if isinstance(other, int):
            if other == 0:
                raise ValueError
            return Rational(numerator=self.numerator,
                            denominator=self.denominator * other)
        raise TypeError

    def __iadd__(self, other):
        if isinstance(other, Rational):
            numerator = self.numerator * other.denominator + self.denominator * other.numerator
            denominator = self.denominator * other.denominator
            return Rational(numerator=numerator,
                            denominator= denominator)
        if isinstance(other, int):
            numerator = self.numerator + self.denominator * other
            denominator = self.denominator
            return Rational(numerator=numerator, denominator=denominator)
        raise TypeError()

    def __isub__(self, other):
        if isinstance(other, Rational):
            numerator = self.numerator * other.denominator - self.denominator * other.numerator
            denominator = self.denominator * other.denominator
            return Rational(numerator=numerator,
                            denominator=denominator)
        if isinstance(other, int):
            numerator = self.numerator - self.denominator * other
            denominator = self.denominator
            return Rational(numerator=numerator, denominator=denominator)
        raise TypeError()

    def __imul__(self, other):
        if isinstance(other, Rational):
            numerator = self.numerator * other.numerator
            denominator = self.denominator * other.denominator
            return Rational(numerator=numerator,
                            denominator=denominator)
        if isinstance(other, int):
            numerator = self.numerator * other.numerator
            denominator = self.denominator
            return Rational(numerator=numerator,
                            denominator=denominator)
        raise TypeError()

    def __idiv__(self, other):
        if isinstance(other, Rational):
            numerator = self.numerator * other.denominator
            denominator = self.denominator * other.numerator
            return Rational(numerator=numerator,
                            denominator=denominator)
        if isinstance(other, int):
            if other == 0:
                raise ValueError
            return Rational(numerator=self.numerator, denominator=self.denominator * other.numerator)
        raise TypeError()

    def show_number(self):
        return f"Number numerator -> {self.numerator} \nNumber denominator -> {self.denominator}"

    def float_format(self):
        return self.numerator / self.denominator

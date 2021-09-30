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
        self.numerator, self.denominator = Rational.__make_it_shorter(a, b)

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

    def show_number(self):
        return f"Number numerator -> {self.numerator} \nNumber denominator -> {self.denominator}"

    def show_in_floatformat(self):
        return f'{self.numerator / self.denominator}'


def main():
    try:
        num = Rational(numerator=5, denominator=10)
        print(num.show_number())
        print(num.show_in_floatformat())
    except Exception as e:
        print(e)


main()

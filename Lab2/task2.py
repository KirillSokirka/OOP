from fractions import Fraction
import math


class Rational:
    """

    """
    def __init__(self, *args, **kwargs):
        a = b = None
        if len(args) == 1 and isinstance(args[0], str):

            a, b = map(int, args[0].split("/"))

            # if not isinstance(number_str, str):
            #     raise Exception("Invalid type, should be string")
            # if number_str.split("/")[1] == "0":
            #     raise Exception("Denominator is zero")
            # temp = number_str.split("/")
            # selflf.numerator, self.denominator = Rational.__make_it_shorter(int(temp[0]), int(temp[1]))
        elif len(kwargs) == 2:
            if not isinstance(kwargs["numerator"], int) or not isinstance(kwargs["denominator"], int):
                raise Exception("Invalid type, should be integer")
            if kwargs["denominator"] == 0:
                raise Exception("Denominator is zero")
            a, b = kwargs.values()
            # self.numerator, self.denominator = Rational.__make_it_shorter(kwargs["numerator"], kwargs["denominator"])
        else:
            raise Exception("Invalid Input")

        self.nu, self.b = Rational.__make_it_shorter(a, b)

    @staticmethod
    def __make_it_shorter(*args):
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
        num = Rational("1/2")
        print(num.show_number())
        print(num.show_in_floatformat())
    except Exception as e:
        print(e)


main()
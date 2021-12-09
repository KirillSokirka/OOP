from Task1.rational_numbers import Rational


class RationalCalculator:

    @staticmethod
    def __validate(a, b):
        if not isinstance(a, Rational):
            raise TypeError("First number is not rational")
        if not isinstance(b, Rational):
            raise TypeError("Second number is not rational")

    @staticmethod
    def sum(a : Rational, b : Rational):
        RationalCalculator.__validate(a, b)
        return a.numerator/a.denominator + b.numerator/b.denominator

    @staticmethod
    def subtract(a: Rational, b: Rational):
        RationalCalculator.__validate(a, b)
        return a.numerator/a.denominator - b.numerator/b.denominator

    @staticmethod
    def multiply(a: Rational, b: Rational):
        RationalCalculator.__validate(a, b)
        return (a.numerator/a.denominator) * (b.numerator/b.denominator)

    @staticmethod
    def divide(a: Rational, b: Rational):
        RationalCalculator.__validate(a, b)
        if b.numerator == 0:
            return None
        return (a.numerator / a.denominator) / (b.numerator / b.denominator)

    @staticmethod
    def compare(a: Rational, b: Rational):
        RationalCalculator.__validate(a, b)
        return a.numerator/a.denominator == b.numerator/b.denominator


if __name__ == '__main__':
    num1 = Rational('1/2')
    num2 = Rational('1/2')
    print(f'Sum {RationalCalculator.sum(num1, num2)}')
    print(f'Subtracting {RationalCalculator.subtract(num1, num2)}')
    print(f'Mult {RationalCalculator.multiply(num1, num2)}')
    print(f'Dividing {RationalCalculator.divide(num1, num2)}')
    print(f'Equals - {RationalCalculator.compare(num1, num2)}')


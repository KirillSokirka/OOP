import sys


def calculate_expression():
    if len(sys.argv) <= 1:
        print("There aren`t expression to calculate")
        return
    try:
        print(eval(''.join(sys.argv[1::])))
    except ZeroDivisionError as e:
        print("Exception information")


calculate_expression()

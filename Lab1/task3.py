import sys


def check_formula(user_input):
    """
        Checks the formula`s correctness and if true: return the result
        of calculation
    :param user_input: arguments from command line
    :return: rightness of formula and
    """
    sign = ['+', '-', '*', '/', '**', '%']
    if user_input[0] in sign or user_input[-1] in sign:
        return False, None
    sign_count = 0
    result = ""
    for el in user_input:
        if el not in sign and not el.isdigit() or sign_count == 2:
            return False, None
        if el in sign:
            sign_count += 1
        else:
            sign_count = 0
        result += el
    return True, eval(result)


def main():
    if len(sys.argv) == 1:
        print("There is no formula to check")
        return
    sys.argv.pop(0)
    right, result = check_formula(''.join(sys.argv))
    print("Input -> ", str(sys.argv), "Right ->", right, "Result ->", result)


main()

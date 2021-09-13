import sys


def check_formula(user_input):
    sign = ['+', '-', '*', '/', '**', '%']
    if user_input[0] in sign or user_input[-1] in sign:
        return False, None
    sign_count = 0
    result = ""
    for el in user_input:
        if el not in sign and not el.isdigit():
            return False, None
        if el in sign:
            sign_count += 1
        else:
            sign_count = 0
        if sign_count == 2:
            return False, None
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

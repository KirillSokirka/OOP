import sys

function_dict = {"sum": "+", "sub": "-", "mult": "*", "div": "/"}


def calculate_expression():
    """
        This function get the data from user, process it and print the result of it.
    """
    if len(sys.argv) == 1:
        return None
    if sys.argv[1] not in function_dict.keys():
        return None
    return eval(sys.argv[2] + function_dict[sys.argv[1]] + sys.argv[3])

try:
    result = calculate_expression()
    if not result:
        print("Error occurred")
    print("Result -> ", result)
except Exception as e:
    print(e)

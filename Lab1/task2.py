import sys

function_dict = {"sum": "+", "sub": "-", "mult": "*", "div": "/"}


def calculate_expression():
    """
        This function get the data from user, process it and print the result of it.
    """
    if len(sys.argv) == 1:
        print("There isn't any expression to calculate")
        return
    try:
        if sys.argv[1] not in function_dict.keys():
            print("Unknown function")
            return
        print("Result -> ", eval(sys.argv[2] + function_dict[sys.argv[1]] + sys.argv[3]))
    except Exception as e:
        print("The error occurred ->", e)


calculate_expression()

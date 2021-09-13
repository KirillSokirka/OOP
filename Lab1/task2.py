import math
import sys


def calculate_expression():
    """
        This function get the data from user, process it and print the result of it.
    """
    if len(sys.argv) == 1:
        print("There isn't any expression to calculate")
        return
    try:
        func, number_of_arguments = get_function(sys.argv[1])
        if not func:
            raise Exception("The unknown function")
        arguments = sys.argv[2::]
        if len(arguments) != number_of_arguments:
            raise Exception("The invalid number of arguments")
        if number_of_arguments == 1:
            print("Result -> ", func(int(arguments[0])))
        elif number_of_arguments == 2:
            print("Result -> ", func(int(arguments[0]), int(arguments[1])))
    except Exception as e:
        print(e)
    except ZeroDivisionError as e:
        print("The error occurred", e)


def get_function(func_name):
    """
        The function checks the function name and return the needed function
    :param func_name: the name of function from user
    :return: lambda function and number of required arguments
    """
    if func_name == "add":
        return lambda x, y: x + y, 2
    if func_name == "sub":
        return lambda x, y: x - y, 2
    if func_name == "mult":
        return lambda x, y: x * y, 2
    if func_name == "div":
        return lambda x, y: x / y, 2
    if func_name == "mod":
        return lambda x, y: x % y, 2
    if func_name == "pow":
        return lambda x, y: x ** y, 2
    if func_name == "cos":
        return lambda x: math.cos(x), 1
    if func_name == "sin":
        return lambda x: math.sin(x), 1
    if func_name == "tan":
        return lambda x: math.tan(x), 1
    return None, None


calculate_expression()

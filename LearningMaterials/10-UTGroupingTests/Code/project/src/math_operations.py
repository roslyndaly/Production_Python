def add(arg1: int, arg2: int):
    return arg1 + arg2

def subtract(arg1: int, arg2: int):
    return arg1 - arg2

def multiply(arg1: int, arg2: int):
    return arg1 * arg2

def divide(arg1: int, arg2: int):
    if arg2 == 0:
        raise ZeroDivisionError('arg2 cannot be 0, since you cannot divide by 0')
    return arg1 / arg2

def power(arg1: float, arg2: float):
    return arg1**arg2

def modulo(arg1: int, arg2: int):
    return arg1 % arg2

def absolute_value(arg):
    return abs(arg)
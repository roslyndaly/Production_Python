"""
module to create mathematical operator functions
"""

def add(num1:int, num2:int) -> int:

    """
    function to do an addition operation
    """
    return num1 + num2

def subtract(num1:int, num2:int) -> int:

    """
    function to do an subtraction operation
    """
    return num1 - num2

def multiply(num1:int, num2:int) -> int:

    """
    function to do an multiplication operation
    """
    return num1 * num2

def divide(num1:int, num2:int) -> float:

    """
    function to do an division operation
    """
    if num2 == 0:
        raise ZeroDivisionError('Argument 2 cannot be 0')
    else:
        return num1/num2


if __name__ == "__main__":
    print("src.math_operations is being executed directly.")
    
import argparse

def calculate_square(square, verbosity=0):
    """
    Calculate the square of a given number with varying verbosity.
    """
    answer = square ** 2
    if verbosity >= 2:
        return f"The square of {square} equals {answer}"
    elif verbosity >= 1:
        return f"{square}^2 == {answer}"
    else:
        return str(answer)

def calculate_power(x, y, verbosity=0):
    """
    Calculate the power of a given base and exponent with varying verbosity.
    """
    answer = x ** y
    if verbosity >= 2:
        return f"{x} to the power {y} equals {answer}"
    elif verbosity >= 1:
        return f"{x}^{y} == {answer}"
    else:
        return str(answer)
    



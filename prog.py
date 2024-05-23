
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
    

def calculate_power_verbose(x, y, verbosity=0):
    """
    Calculate the power of a given base and exponent with varying verbosity, including file name in verbose mode.
    """
    output = ""
    answer = x ** y
    if verbosity >= 2:
        output += f"Running '{__file__}'\n"
    if verbosity >= 1:
        output += f"{x}^{y} == {answer}\n"
    output += str(answer)
    return output

def power_conflict(args, x, y, verbosity=0):
    """
    Calculate the power of a given base and exponent with support for quiet and verbose output modes.
    """
    answer = x ** y
    if args.quiet:
        return str(answer)
    elif args.verbose:
        output = ""
        if args.verbosity >= 2:
            output += f"Running '{__file__}'\n"
        if args.verbosity >= 1:
            output += f"{x}^{y} == {answer}\n"
        return output
    else:
        return f"{x}^{y} == {answer}"
    

    

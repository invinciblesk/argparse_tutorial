import argparse
from prog import calculate_square, calculate_power, calculate_power_verbose, power_conflict

def get_args():
    parser = argparse.ArgumentParser(description="Perform calculations with varying verbosity.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_square = subparsers.add_parser('square', help="Calculate the square of a number")
    parser_square.add_argument('square', type=int, help="The number to be squared")
    parser_square.add_argument('-v', '--verbosity', type=int, choices=[0, 1, 2], default=0, help="Increase output verbosity")

    parser_power = subparsers.add_parser('power', help="Calculate the power of a base number")
    parser_power.add_argument('x', type=int, help="The base number")
    parser_power.add_argument('y', type=int, help="The exponent")
    parser_power.add_argument('-v', '--verbosity', type=int, choices=[0, 1, 2], default=0, help="Increase output verbosity")

    parser_power_verbose = subparsers.add_parser('power_verbose', help="Calculate the power with file name in verbose mode")
    parser_power_verbose.add_argument('x', type=int, help="The base number")
    parser_power_verbose.add_argument('y', type=int, help="The exponent")
    parser_power_verbose.add_argument('-v', '--verbosity', type=int, choices=[0, 1, 2], default=0, help="Increase output verbosity")

    
    return parser.parse_args()

def main():
    args = get_args()
    if args.command == 'square':
        print(calculate_square(args.square, args.verbosity))
    elif args.command == 'power':
        print(calculate_power(args.x, args.y, args.verbosity))
    elif args.command == 'power_verbose':
        print(calculate_power_verbose(args.x, args.y, args.verbosity))
    elif args.command == 'power_conflict':
        print(power_conflict(args, args.x, args.y))

if __name__ == "__main__":
    main()

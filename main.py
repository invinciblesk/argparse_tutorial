import argparse

def main():
    parser = argparse.ArgumentParser(description="calculate X to the power of Y")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true", help="Print verbose output")
    group.add_argument("-q", "--quiet", action="store_true", help="Print only the result")
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    args = parser.parse_args()

if __name__ == "__main__":
    main()

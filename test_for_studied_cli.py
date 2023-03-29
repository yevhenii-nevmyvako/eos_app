import argparse


def add(a, b):
    """Learn how to implement Cli by this manual func"""
    return a + b


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    args = parser.parse_args()
    print(add(args.a, args.b))


if __name__ == "__main__":
    main()

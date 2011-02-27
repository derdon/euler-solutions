from itertools import imap
import sys


def square(x):
    return x ** 2


def sum_of_squares(numbers):
    return sum(imap(square, numbers))


def square_of_sums(numbers):
    return square(sum(numbers))


def main(x):
    seq = xrange(1, x + 1)
    return square_of_sums(seq) - sum_of_squares(seq)


if __name__ == '__main__':
    try:
        x = int(sys.argv[1])
    except (IndexError, ValueError):
        x = 100
    print main(x)

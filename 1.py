from itertools import ifilter


def is_multiple_of_three_or_five(num):
    return num % 3 == 0 or num % 5 == 0


def main():
    return sum(ifilter(is_multiple_of_three_or_five, xrange(1000)))


if __name__ == '__main__':
    print main()

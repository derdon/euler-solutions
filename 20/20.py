from itertools import imap
import math


def main():
    return sum(imap(int, str(math.factorial(100))))


if __name__ == '__main__':
    print main()

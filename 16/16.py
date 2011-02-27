# (c) Simon Liedtke <liedtke.simon@googlemail.com> under the ISC license.
# See COPYING for more details.


def main():
from itertools import imap
import sys


def main(x):
    return sum(imap(int, str(2 ** x)))


if __name__ == '__main__':
    try:
        x = int(sys.argv[1])
    except (IndexError, ValueError):
        x = 1000
    print main(x)

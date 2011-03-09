# (c) Simon Liedtke <liedtke.simon@googlemail.com> under the ISC license.
# See COPYING for more details.


from fractions import gcd


def lcm(a, b):
    return a * b / gcd(a, b)


def main():
    return reduce(lcm, xrange(2, 21))


if __name__ == '__main__':
    print main()

from fractions import gcd


def lcm(a, b):
    return a * b / gcd(a, b)


def main():
    return reduce(lcm, xrange(2, 21))


if __name__ == '__main__':
    print main()

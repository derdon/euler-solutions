def main():
    return sum(y for y in xrange(1000) if any(not y % x for x in [3, 5]))


if __name__ == '__main__':
    print main()

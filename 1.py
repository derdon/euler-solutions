def main():
    return sum(num for num in xrange(1000) if any(not num % x for x in [3, 5]))


if __name__ == '__main__':
    print main()

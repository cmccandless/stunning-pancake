#!/usr/bin/env python
# https://projecteuler.net/problem=10


def sieve(limit=1000000):
    notPrime = set()
    for x in range(2, limit):
        if x in notPrime:
            continue
        yield x
        for i in range(x, limit, x):
            notPrime.add(i)


def run():
    print(sum(sieve(2000000)))


if __name__ == '__main__':
    run()

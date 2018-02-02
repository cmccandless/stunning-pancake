#!/usr/bin/env python
# https://projecteuler.net/problem=12
import unittest
from functools import reduce
from operator import mul


def sieve(limit=1000000):
    yield 2
    np = set()
    for x in range(3, limit, 2):
        if x in np:
            continue
        yield x
        np.update(range(x + x, limit, x))


primes = list(sieve())


def factor_count(n):
    if n == 1:
        return 0
    counts = []
    for p in primes:
        if n % p == 0:
            counts.append(1)
            while n % p == 0:
                counts[-1] += 1
                n //= p
        if n == 1:
            return reduce(mul, counts)


def answer():
    target, x, count = (500, 1, 2)
    while factor_count(x) <= target:
        x, count = (x + count, count + 1)
    return x


def run():
    print(answer())


class Test12(unittest.TestCase):
    def test_expected(self):
        expected = 76576500
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

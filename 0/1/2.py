#!/usr/bin/env python
# https://projecteuler.net/problem=12
import unittest
from math import sqrt

factors_of = {}


def factor(n):
    factors = {1, n}
    for i in range(2, int(sqrt(n)) + 1):
        if n % i != 0:
            continue
        for f in (factors_of.get(i, None) or factor(i)):
            factors.add(f)
            factors.add(n // f)
    factors_of[n] = factors
    return factors


def answer():
    target, x, count = (500, 1, 2)
    while len(factor(x)) <= target:
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

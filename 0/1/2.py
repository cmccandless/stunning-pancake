#!/usr/bin/env python
# https://projecteuler.net/problem=12
import unittest
from math import sqrt

factors_of = {}


def triangle_numbers():
    x = 1
    count = 1
    while True:
        yield x
        count += 1
        x += count


def factor(n):
    if n in factors_of:
        return factors_of[n]
    factors = {1, n}
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            ifactors = factor(i)
            for f in ifactors:
                factors.add(f)
                factors.add(n / f)
    factors_of[n] = factors
    return factors


def answer():
    target = 500
    tri_gen = triangle_numbers()
    while True:
        x = next(tri_gen)
        factors = factor(x)
        if len(factors) > target:
            return x


def run():
    print(answer())


class Test12(unittest.TestCase):
    def test_expected(self):
        with open('../../answers.txt') as f:
            expected = int(f.readlines()[12])
        # expected = 76576500
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

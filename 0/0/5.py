#!/usr/bin/env python
# https://projecteuler.net/problem=5
import unittest
from itertools import groupby
from functools import reduce


def prime_factors(n):
    not_prime = {0, 1}
    limit = n + 1
    for x in range(2, limit):
        if x in not_prime:
            continue
        while n >= x and n % x == 0:
            yield x
            n /= x
        if n == 1:
            raise StopIteration()
        for y in range(x + x, limit, x):
            not_prime.add(y)


def smallest_divisible(max_divisor, min_divisor=2):
    m = {}
    for n in range(min_divisor, max_divisor + 1):
        fs = prime_factors(n)
        for k, g in groupby(fs):
            m[k] = max(m.get(k, 0), len(list(g)))
    print(m)
    return reduce(lambda a, t: a * pow(*t), m.items(), 1)


def answer():
    return smallest_divisible(20)


def run():
    print(answer())


class Test5(unittest.TestCase):
    def test_expected(self):
        expected = 232792560
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

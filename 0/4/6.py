#!/usr/bin/env python
# https://projecteuler.net/problem=46
import unittest
from math import sqrt


def not_perfect_square(n):
    sq = sqrt(n)
    return int(sq) != sq


def answer(limit=1000000):
    primes = {2, 3, 5, 7}
    not_prime = {0, 1}
    for x in range(9, limit, 2):
        if x in not_prime:
            if all(
                not_perfect_square((x - p) >> 1)
                for p in primes
            ):
                return x
            continue
        primes.add(x)
        for y in range(x + x, limit, x):
            not_prime.add(y)


def run():
    print(answer())


class Test46(unittest.TestCase):
    def test_expected(self):
        expected = 5777
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

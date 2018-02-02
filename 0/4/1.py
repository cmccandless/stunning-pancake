#!/usr/bin/env python
# https://projecteuler.net/problem=41
import unittest
from itertools import permutations


def sieve(limit=100000):
    yield 2
    not_prime = set()
    for i in range(3, limit, 2):
        if i in not_prime:
            continue
        yield i
        not_prime.update(range(i + i, limit, i))


def answer():
    primes = set(sieve())
    s = '987654321'
    while s:
        for p in map(int, map(''.join, permutations(s))):
            if (
                p % 2 != 0 and
                (
                    p in primes or
                    not any(p % x == 0 for x in primes)
                )
            ):
                return p
        s = s[1:]


def run():
    print(answer())


class Test41(unittest.TestCase):
    def test_expected(self):
        expected = 7652413
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

#!/usr/bin/env python
# https://projecteuler.net/problem=33
import unittest
from math import gcd, floor
from functools import reduce
from operator import mul


def answer():
    results = []
    for a in range(10, 100):
        for b in range(a + 1, 100):
            if b % 10 == 0:
                continue
            if a % 10 == floor(b / 10):
                if a / b == floor(a / 10) / (b % 10):
                    results.append((a, b))
    numerator, denominator = reduce(
        lambda t, t2: tuple(
            map(
                lambda _t: mul(*_t),
                zip(t, t2)
            )
        ),
        results,
        (1, 1)
    )
    return denominator // gcd(numerator, denominator)


def run():
    print(answer())


class Test33(unittest.TestCase):
    def test_expected(self):
        expected = 100
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

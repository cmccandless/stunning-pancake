#!/usr/bin/env python
# https://projecteuler.net/problem=44
import unittest
from math import sqrt


def is_pentagonal(x):
    return (sqrt(1 + 24 * x) + 1) % 6 == 0


def answer():
    pentagonals = []
    i = 1
    while True:
        i += 1
        n = ((3 * i - 1) * i) // 2
        for m in pentagonals:
            d = n - m
            # if is_pentagonal(d) and is_pentagonal(n + m):
            if d in pentagonals and is_pentagonal(n + m):
                return d
        pentagonals.insert(0, n)


def run():
    print(answer())


class Test44(unittest.TestCase):
    def test_expected(self):
        expected = 5482660
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

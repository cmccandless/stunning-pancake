#!/usr/bin/env python
# https://projecteuler.net/problem=45
import unittest
from math import sqrt


def is_pentagonal(x):
    return (sqrt(1 + 24 * x) + 1) % 6 == 0


def is_hexagonal(x):
    return (sqrt(1 + 8 * x) + 1) % 4 == 0


def answer(start=285):
    while True:
        start += 1
        t = start * (start + 1) // 2
        if is_pentagonal(t) and is_hexagonal(t):
            return t


def run():
    print(answer())


class Test45(unittest.TestCase):
    def test_expected(self):
        expected = 1533776805
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

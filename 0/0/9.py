#!/usr/bin/env python
# https://projecteuler.net/problem=9
import unittest
from math import sqrt


def is_triplet(a, b, c):
    return a * a + b * b == c * c


def answer():
    target = 1000
    limit = 10000
    for a in range(1, limit):
        for b in range(1, a):
            c = int(sqrt(a * a + b * b))
            if a + b + c == target:
                return a * b * c


def run():
    print(answer())


class Test9(unittest.TestCase):
    def test_expected(self):
        with open('../../answers.txt') as f:
            expected = int(f.readlines()[9])
        # expected = 35541072
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

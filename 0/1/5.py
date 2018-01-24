#!/usr/bin/env python
# https://projecteuler.net/problem=15
import unittest
from functools import reduce
from operator import mul


def factorial(n):
    return reduce(mul, range(2, n + 1), 1)


def answer(limit=20):
    paths = [1] * (limit + 1)
    for _ in range(limit):
        for i in range(1, limit + 1):
            paths[i] += paths[i - 1]
    return paths[limit]


def run():
    print(answer(2))
    print(answer())


class Test15(unittest.TestCase):
    def test_expected(self):
        expected = 137846528820
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

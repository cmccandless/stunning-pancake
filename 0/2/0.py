#!/usr/bin/env python
# https://projecteuler.net/problem=20
import unittest
from functools import reduce
from operator import mul


def factorial(n):
    return reduce(mul, range(2, n + 1))


def answer(n=100):
    return sum(map(int, str(factorial(n))))


def run():
    print(answer(10))  # 27
    print(answer())


class Test20(unittest.TestCase):
    def test_expected(self):
        expected = 648
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

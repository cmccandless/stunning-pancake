#!/usr/bin/env python
# https://projecteuler.net/problem=24
import unittest
from itertools import permutations


def answer(nth=1000000):
    nth -= 1
    for i, n in enumerate(permutations('0123456789')):
        if i == nth:
            return int(''.join(n))


def run():
    print(answer())


class Test24(unittest.TestCase):
    def test_expected(self):
        expected = 2783915460
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

#!/usr/bin/env python
# https://projecteuler.net/problem=72
# Discussion: https://projecteuler.net/thread=72
from __future__ import division
import unittest


def answer(limit=1000000):
    limit += 1
    totient = list(range(limit))
    totient[1] = 0
    totient[2] = 1
    for y in range(4, limit, 2):
        totient[y] >>= 1
    for x in range(3, limit, 2):
        if totient[x] == x:
            totient[x] -= 1
            factor = totient[x] / x
            for y in range(x + x, limit, x):
                totient[y] *= factor
    return sum(totient)


def run():
    print(answer())


class Test72(unittest.TestCase):
    def test_expected(self):
        expected = 303963552391
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

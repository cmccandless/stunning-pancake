#!/usr/bin/env python
# https://projecteuler.net/problem=64
# Discussion: https://projecteuler.net/thread=64
from __future__ import division
import unittest
from fractions import gcd
from math import sqrt


def period_length(i):
    sq = sqrt(i)
    a0 = a = int(sq)
    if sq == a:
        return 0
    n, d = (1, -a)
    visited = set()
    while True:
        d_next = i - d * d
        __gcd__ = gcd(n, d_next)
        n_next = n // __gcd__ * (a0 - d)
        n = d_next // __gcd__
        a, d = divmod(n_next, n)
        d -= a0
        if (a, n, d) in visited:
            break
        visited.add((a, n, d))
    return len(visited)


def answer(limit=10000):
    count = 0
    for i in range(2, limit + 1):
        if period_length(i) & 1:
            count += 1
    return count


def run():
    print(answer())


class Test64(unittest.TestCase):
    def test_expected(self):
        expected = 1322
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

#!/usr/bin/env python
# https://projecteuler.net/problem=23
import unittest
from math import sqrt
from itertools import takewhile


def answer():
    limit = 28124
    result_limit = 20162
    abundant = [
        n for n in range(12, limit)
        if n <= sum({
            f
            for i in range(2, int(sqrt(n)) + 1)
            if n % i == 0
            for f in (i, n // i)
        })
    ]
    s_abundant = set(abundant)
    return 276 + sum(
        x for x in range(25, result_limit)
        if all(
            x - a not in s_abundant
            for a in takewhile(x.__gt__, abundant)
        )
    )


def run():
    print(answer())


class Test23(unittest.TestCase):
    def test_expected(self):
        expected = 4179871
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

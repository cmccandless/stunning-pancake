#!/usr/bin/env python
# https://projecteuler.net/problem=23
import unittest
from math import sqrt


def is_abundant(n):
    divs = {1}
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return n < sum(divs)


def answer():
    limit = 28124
    abundant = set(filter(is_abundant, range(12, limit)))
    return sum(
        x for x in range(1, limit)
        if all(x - a not in abundant for a in abundant)
    )


def run():
    print(answer())


class Test23(unittest.TestCase):
    def test_expected(self):
        expected = 4179871
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

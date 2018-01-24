#!/usr/bin/env python
# https://projecteuler.net/problem=21
import unittest
from math import sqrt


def d(n):
    divs = {1}
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return sum(divs)


def answer(limit=10000):
    amicable = set()
    not_amicable = set()
    for a in range(2, limit):
        if a in amicable or a in not_amicable:
            continue
        b = d(a)
        if d(b) == a and a != b:
            amicable.add(a)
            amicable.add(b)
        else:
            not_amicable.add(a)
            not_amicable.add(b)
    return sum(amicable)


def run():
    for x in [220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368]:
        print(x, d(x))
    print(answer())


class Test21(unittest.TestCase):
    def test_expected(self):
        expected = 31626
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

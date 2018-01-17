#!/usr/bin/env python
# https://projecteuler.net/problem=3
import unittest
from math import sqrt


def answer():
    target = 600851475143
    notPrime = set()
    limit = round(sqrt(target))
    i = 1
    while target > 1 and i < limit:
        i += 2
        if i in notPrime:
            continue
        while target >= i and target % i == 0:
            target = target / i
        for j in range(i + i, limit, i):
            notPrime.add(j)
    return i


def run():
    print(answer())


class Test3(unittest.TestCase):
    def test_expected(self):
        expected = 6857
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

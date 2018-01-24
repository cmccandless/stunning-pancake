#!/usr/bin/env python
# https://projecteuler.net/problem=34
import unittest

factorial = {
    0: 1,
    1: 1,
    2: 2,
    3: 6,
    4: 24,
    5: 120,
    6: 720,
    7: 5040,
    8: 40320,
    9: 362880,
}


def answer():
    total = 0
    limit = 50000
    for x in range(10, limit):
        if sum(map(factorial.get, map(int, str(x)))) == x:
            total += x
        x += 1
    return total


def run():
    print(answer())


class Test34(unittest.TestCase):
    def test_expected(self):
        expected = 40730
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

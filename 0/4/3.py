#!/usr/bin/env python
# https://projecteuler.net/problem=43
import unittest
from itertools import permutations


def perm_str(n):
    return map(''.join, permutations(n))


divisors = list(zip(range(1, 8), [2, 3, 5, 7, 11, 13, 17]))


def match(p):
    return all(int(p[i:i + 3]) % d == 0 for i, d in divisors)


def answer():
    return sum(
        int(p) for p in perm_str('0123456789')
        if match(p)
    )


def run():
    # print(match('1406357289'))
    print(answer())


class Test43(unittest.TestCase):
    def test_expected(self):
        expected = 16695334890
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

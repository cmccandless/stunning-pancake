#!/usr/bin/env python
# https://projecteuler.net/problem=38
import unittest
from itertools import permutations


def check(pandigital):
    for i in range(5, 0, -1):
        sp = str(pandigital)
        a = int(sp[:i])
        sp = sp[i:]
        b = a + a
        sb = str(b)
        while sp and sp.startswith(sb):
            sp = sp[len(sb):]
            b += a
            sb = str(b)
        if not sp:
            return True
    return False


def answer():
    for p in map(int, map(''.join, permutations('987654321'))):
        if check(p):
            return p


def run():
    # print(check(192384576))
    # print(check(123456789))
    print(answer())


class Test38(unittest.TestCase):
    def test_expected(self):
        expected = 932718654
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

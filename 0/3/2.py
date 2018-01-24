#!/usr/bin/env python
# https://projecteuler.net/problem=32
import unittest
from itertools import permutations


def answer():
    results = set()
    for p in map(''.join, permutations('123465789')):
        right = int(p[5:])
        for digits in [3, 4]:
            a = int(p[:digits])
            b = int(p[digits:5])
            if right == a * b:
                results.add(right)
                break
    return sum(results)


def run():
    print(answer())


class Test32(unittest.TestCase):
    def test_expected(self):
        expected = 45228
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

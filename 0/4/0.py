#!/usr/bin/env python
# https://projecteuler.net/problem=40
import unittest


def answer(indices=[1, 10, 100, 1000, 10000, 100000, 1000000]):
    d = 0
    n = 0
    result = 1
    while indices:
        n += 1
        for ch in str(n):
            d += 1
            if d == indices[0]:
                indices.pop(0)
                result *= int(ch)
            if not indices:
                break
    return result


def run():
    print(answer())


class Test40(unittest.TestCase):
    def test_expected(self):
        expected = 210
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

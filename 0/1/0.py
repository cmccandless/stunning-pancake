#!/usr/bin/env python
# https://projecteuler.net/problem=10
import unittest


def answer():
    total = 2
    limit = 2000000
    np = set()
    for x in range(3, limit, 2):
        if x in np:
            continue
        total += x
        for i in range(x + x, limit, x):
            np.add(i)
    return total


def run():
    print(answer())


class Test10(unittest.TestCase):
    def test_expected(self):
        expected = 142913828922
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

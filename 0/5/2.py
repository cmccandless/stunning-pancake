#!/usr/bin/env python
# https://projecteuler.net/problem=52
# Discussion: https://projecteuler.net/thread=52
import unittest


def answer():
    n = 123456
    while True:
        base = set(str(n))
        if all(set(str(n * i)) == base for i in range(2, 7)):
            return n
        n += 1


def run():
    print(answer())


class Test52(unittest.TestCase):
    def test_expected(self):
        expected = 142857
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

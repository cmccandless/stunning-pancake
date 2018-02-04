#!/usr/bin/env python
# https://projecteuler.net/problem=71
# Discussion: https://projecteuler.net/thread=71
import unittest


def answer(limit=1000000):
    a, b = (2, 5)
    c, d = (3, 7)
    b += d
    while b <= limit:
        a += c
        b += d
    return a


def run():
    print(answer())


class Test71(unittest.TestCase):
    def test_expected(self):
        expected = 428570
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

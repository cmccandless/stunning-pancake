#!/usr/bin/env python
# https://projecteuler.net/problem=1
import unittest


def mults_of(n, under):
    return {x for x in range(n, under, n)}


def answer():
    under = 1000
    return sum(mults_of(3, under).union(mults_of(5, under)))


def run():
    print(answer())


class Test1(unittest.TestCase):
    def test_expected(self):
        expected = 233168
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

#!/usr/bin/env python
# https://projecteuler.net/problem=16
import unittest


def answer(exp=1000):
    return sum(map(int, str(pow(2, exp))))


def run():
    print(answer(15))
    print(answer())


class Test16(unittest.TestCase):
    def test_expected(self):
        expected = 1366
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

#!/usr/bin/env python
# https://projecteuler.net/problem=36
import unittest


def is_palindrome(s):
    return s == s[::-1]


def answer(limit=1000000):
    return sum(
        x for x in range(1, limit)
        if is_palindrome(str(x)) and is_palindrome('{:b}'.format(x))
    )


def run():
    print(answer())


class Test36(unittest.TestCase):
    def test_expected(self):
        expected = 872187
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

#!/usr/bin/env python
# https://projecteuler.net/problem=7
import unittest


def answer():
    nth = 10001
    limit = 1000000
    x = c = 1
    not_prime = set()
    while c < nth and x < limit:
        x += 2
        if x in not_prime:
            continue
        c += 1
        if c == nth:
            continue
        for i in range(x + x, limit, x):
            not_prime.add(i)
    return x


def run():
    print(answer())


class Test7(unittest.TestCase):
    def test_expected(self):
        expected = 104743
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

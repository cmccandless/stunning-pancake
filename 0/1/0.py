#!/usr/bin/env python
# https://projecteuler.net/problem=10
import unittest


def sieve(limit=1000000):
    notPrime = set()
    yield 2
    for x in range(3, limit, 2):
        if x in notPrime:
            continue
        yield x
        for i in range(x, limit, x):
            notPrime.add(i)


def answer():
    return sum(sieve(2000000))


def run():
    print(answer())


class Test10(unittest.TestCase):
    def test_expected(self):
        expected = 142913828922
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

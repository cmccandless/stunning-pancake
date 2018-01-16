#!/usr/bin/env python
# https://projecteuler.net/problem=7
import unittest


def sieve(limit=1000000):
    notPrime = set()
    for x in range(2, limit):
        if x in notPrime:
            continue
        yield x
        for i in range(x, limit, x):
            notPrime.add(i)


def answer():
    sieve_gen = sieve()
    for i in range(10001):
        x = next(sieve_gen)
    return x


def run():
    print(answer())


class Test7(unittest.TestCase):
    def test_expected(self):
        with open('../../answers.txt') as f:
            expected = int(f.readlines()[7])
        # expected = 104743
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

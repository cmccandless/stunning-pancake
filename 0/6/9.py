#!/usr/bin/env python
# https://projecteuler.net/problem=69
# Discussion: https://projecteuler.net/thread=69
import unittest


def sieve(limit=1000000):
    if limit > 2:
        yield 2
    np = set()
    for x in range(3, limit, 2):
        if x in np:
            continue
        yield x
        np.update(range(x + x, limit, x))


def answer(limit=1000000):
    primes = list(sieve(limit))
    n = 1
    while True:
        p = primes.pop(0)
        if n * p > limit:
            break
        n *= p
    return n


def run():
    print(answer())


class Test69(unittest.TestCase):
    def test_expected(self):
        expected = 510510
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

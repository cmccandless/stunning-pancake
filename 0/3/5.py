#!/usr/bin/env python
# https://projecteuler.net/problem=35
import unittest


def rotations(x):
    yield x
    y = x[1:] + x[:1]
    while y != x:
        yield y
        y = y[1:] + y[:1]


def sieve(limit=1000000):
    yield 2
    not_prime = set()
    for x in range(3, limit, 2):
        if x in not_prime:
            continue
        yield x
        not_prime.update(range(x + x, limit, x))


def answer(limit=1000000):
    primes = set(sieve(limit))
    count = 0
    for p in primes:
        if all(r in primes for r in map(int, rotations(str(p)))):
            count += 1
    return count


def run():
    print(answer())


class Test35(unittest.TestCase):
    def test_expected(self):
        expected = 55
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

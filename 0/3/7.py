#!/usr/bin/env python
# https://projecteuler.net/problem=37
import unittest


def sieve(limit=1000000):
    yield 2
    not_prime = set()
    for x in range(3, limit, 2):
        if x in not_prime:
            continue
        yield x
        for y in range(x + x, limit, x):
            not_prime.add(y)


primes = set(sieve())


def truncatable(prime):
    p = prime
    c = 0
    pow10 = 0
    while p > 0:
        if p not in primes:
            return False
        p, q = divmod(p, 10)
        c = q * pow(10, pow10) + c
        if c not in primes:
            return False
        pow10 += 1
    return True


def answer(limit=1000000):
    primes = list(sieve(limit))
    return sum(filter(truncatable, primes[4:]))


def run():
    print(answer())


class Test37(unittest.TestCase):
    def test_expected(self):
        expected = 748317
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

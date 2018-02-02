#!/usr/bin/env python
# https://projecteuler.net/problem=26
import unittest


def sieve(limit=10000):
    not_prime = set()
    for x in range(2, limit):
        if x in not_prime:
            continue
        yield x
        not_prime.update(range(x + x, limit, x))


def mult_order(n):
    x = 10
    k = 1
    while x % n != 1:
        x *= 10
        k += 1
    return k


def answer(limit=1000):
    primes = list(sieve(limit))[3:]
    return max(
        zip(map(mult_order, primes), primes)
    )[1]


def run():
    # print(answer(10))
    # print(answer(100))
    print(answer())


class Test26(unittest.TestCase):
    def test_expected(self):
        expected = 983
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

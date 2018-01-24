#!/usr/bin/env python
# https://projecteuler.net/problem=27
import unittest


def sieve(limit=100000):
    not_prime = {0, 1}
    for i in range(2, limit):
        if i in not_prime:
            continue
        yield i
        for x in range(i + i, limit, i):
            not_prime.add(x)


def quadratic_prime_generator(a, b, primes):
    x, n = (b, 0)
    while x in primes:
        n += 1
        x = (n + a) * n + b
    return n


def answer(limit=1000):
    primes = set(sieve())
    coeff_prod = 0
    num_primes = 0
    lower = -limit
    upper = limit + 1
    for a in range(lower, upper):
        for b in range(a, upper):
            count = quadratic_prime_generator(a, b, primes)
            if count > num_primes:
                coeff_prod = a * b
                num_primes = count
    return coeff_prod


def run():
    print(answer())


class Test27(unittest.TestCase):
    def test_expected(self):
        expected = -59231
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

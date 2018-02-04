#!/usr/bin/env python
# https://projecteuler.net/problem=58
# Discussion: https://projecteuler.net/thread=58
from __future__ import division
import unittest


def corners(n):
    x = n * n
    # yield x
    inc = n - 1
    if n > 1:
        for _ in range(3):
            x -= inc
            yield x


_known_primes = set()


def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n - 1:
            return False
    return True


def is_prime(n, k=16):
    if n in (0, 1):
        return False
    if n in _known_primes:
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while d & 1 == 0:
        d, s = (d >> 1, s + 1)
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(
            _try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13)
        )
    if n < 341550071728321:
        return not any(
            _try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17)
        )
    # otherwise
    return not any(_try_composite(a, d, n, s) for a in _known_primes[:k])


_known_primes = {x for x in range(3, 1000, 2) if is_prime(x)}
_known_primes.add(2)
_known_primes.add(3)


def answer():
    diagonal_primes = 3
    diagonal_total = 5
    target = 0.1
    side_length = 3
    ratio = diagonal_primes / diagonal_total
    while ratio >= target:
        side_length += 2
        for c in corners(side_length):
            if is_prime(c):
                diagonal_primes += 1
        diagonal_total += 4
        ratio = diagonal_primes / diagonal_total
    return side_length


def run():
    print(answer())


class Test58(unittest.TestCase):
    def test_expected(self):
        expected = 26241
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

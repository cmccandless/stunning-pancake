#!/usr/bin/env python
# https://projecteuler.net/problem=47
import unittest


def sieve(limit=680):
    yield 2
    np = set()
    for x in range(3, limit, 2):
        if x in np:
            continue
        yield x
        np.update(range(x + x, limit, x))


# primes = list(sieve())
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 31, 47, 83, 491, 677]
p_set = set(primes)


def prime_factors(n):
    for p in primes:
        if n == 1:
            break
        elif n in p_set:
            yield n
            break
        elif n % p == 0:
            yield p
            while n % p == 0:
                n //= p


def answer():
    remaining = limit = 4
    num = 0
    n = 646
    used = set()
    while remaining != 0:
        n += 1
        pfs = set(prime_factors(n))
        used = used.union(pfs)
        if len(pfs) == limit:
            if remaining == limit:
                num = n
            remaining -= 1
        else:
            remaining = limit
    return num


def run():
    print(answer())


class Test47(unittest.TestCase):
    def test_expected(self):
        expected = 134043
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

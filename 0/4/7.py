#!/usr/bin/env python
# https://projecteuler.net/problem=47
import unittest


def sieve(limit=100000):
    yield 2
    np = set()
    for x in range(3, limit, 2):
        if x in np:
            continue
        yield x
        for y in range(x + x, limit, x):
            np.add(y)


primes = list(sieve())


def prime_factors(n):
    for p in primes:
        if n == 1:
            break
        while n % p == 0:
            yield p
            n //= p


def answer():
    nums = []
    limit = 4
    n = 646
    while len(nums) < limit:
        n += 1
        pfs = set(prime_factors(n))
        if len(pfs) == limit:
            nums.append(n)
        else:
            nums = []
    print(nums)
    return nums[0]


def run():
    print(answer())


class Test47(unittest.TestCase):
    def test_expected(self):
        expected = 134043
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

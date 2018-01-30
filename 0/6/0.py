#!/usr/bin/env python
# https://projecteuler.net/problem=60
# Discussion: https://projecteuler.net/thread=60
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


_known_primes = set(sieve(1000))


# Modified Miller-Rabin algorithm
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

    def _try_composite(a, d, n, s):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n - 1:
                return False
        return True
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    return not any(_try_composite(a, d, n, s) for a in (2, 3))


def answer():
    prime_list = list(sieve(10000))[1:]
    primes_with_str = list(
        zip(
            range(1, len(prime_list) + 1),
            map(str, prime_list),
            prime_list
        )
    )
    c_able = {
        pa: {
            pb for _, sb, pb in primes_with_str[i:]
            if is_prime(int(sa + sb)) and is_prime(int(sb + sa))
        }
        for i, sa, pa in primes_with_str
    }
    return next(
        pa + pb + pc + pd + pe
        for pa, ca in ((pa, c_able[pa]) for pa in c_able)
        for pb, cab in ((pb, ca.intersection(c_able[pb])) for pb in ca)
        for pc, cabc in ((pc, cab.intersection(c_able[pc])) for pc in cab)
        for pd, cabcd in ((pd, cabc.intersection(c_able[pd])) for pd in cabc)
        for pe in cabcd
    )


def run():
    print(answer())


class Test60(unittest.TestCase):
    def test_expected(self):
        expected = 26033
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

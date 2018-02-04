#!/usr/bin/env python
# https://projecteuler.net/problem=60
# Discussion: https://projecteuler.net/thread=60
import unittest


def sieve(limit):
    yield 2
    np = set()
    for x in range(3, limit, 2):
        if x in np:
            continue
        yield x
        np.update(range(x + x, limit, x))


_known_primes = set(sieve(100))


# Modified Miller-Rabin algorithm
def is_prime(n, k=16):
    if n < 2:
        return False
    if n in _known_primes:
        return True
    for p in _known_primes:
        if n % p == 0:
            return False
    m = n - 1
    d, s = m, 0
    while d & 1 == 0:
        d, s = (d >> 1, s + 1)

    if pow(2, d, n) != 1:
        i = 0
        while i < s and pow(2, (1 << i) * d, n) != m:
            i += 1
        if i == s:
            return False
    return True


def answer():
    mod10 = {1, 3, 7, 9}
    primes_with_str = [
        (i, str(p), p)
        for i, p in enumerate(
            p for p in sieve(8390)
            if p % 10 in mod10
        )
    ][3:]
    c_able = {
        a: {
            b for _, sb, b in primes_with_str[i:]
            if is_prime(int(sa + sb)) and is_prime(int(sb + sa))
        }
        for i, sa, a in primes_with_str
    }
    # 13 5197 5701 6733 8389
    return next(
        a + b + c + d + e
        for a, ca in c_able.items()
        for b, cab in ((b, ca.intersection(c_able[b])) for b in ca)
        for c, cabc in ((c, cab.intersection(c_able[c])) for c in cab)
        for d, cabcd in ((d, cabc.intersection(c_able[d])) for d in cabc)
        for e in cabcd
    )


def run():
    print(answer())


class Test60(unittest.TestCase):
    def test_expected(self):
        expected = 26033
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

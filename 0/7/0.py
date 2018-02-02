#!/usr/bin/env python
# https://projecteuler.net/problem=70
# Discussion: https://projecteuler.net/thread=70
import unittest


def sieve(limit=5000, minimum=2000):
    np = set()
    for x in range(3, limit, 2):
        if x in np:
            continue
        if x > minimum:
            yield x
        np.update(range(x + x, limit, x))


def answer():
    primes = list(sieve())
    return min(
        (
            (x, y)
            for x, y in (
                (ab, (a - 1) * (b - 1))
                for ab, a, b in (
                    (a * b, a, b)
                    for i, a in enumerate(primes)
                    for b in primes[i + 1:]
                )
                if ab < 10000000
            )
            if sorted(str(x)) == sorted(str(y))
        ),
        key=lambda t: t[0] / t[1]
    )[0]


def run():
    print(answer())


class Test70(unittest.TestCase):
    def test_expected(self):
        expected = 8319823
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

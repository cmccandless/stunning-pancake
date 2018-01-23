#!/usr/bin/env python
# https://projecteuler.net/problem=49
import unittest
from itertools import permutations


def sieve(limit=10000):
    yield 2
    np = set()
    for x in range(3, limit, 2):
        if x in np:
            continue
        yield x
        for y in range(x + x, limit, x):
            np.add(y)


def answer():
    primes = list(sieve())
    p_set = set(primes)
    for p_base in primes:
        if p_base > 3000:
            break
        if p_base < 1488:
            continue
        p_perms = sorted({
            p for p in map(int, map(''.join, permutations(str(p_base))))
            if p in p_set
        })
        if len(p_perms) < 3 or p_perms[0] != p_base:
            continue
        if len(p_perms) == 3:
            if p_perms[1] - p_perms[0] == p_perms[2] - p_perms[1]:
                return int(''.join(map(str, p_perms)))
        else:
            for perm in permutations(p_perms, 3):
                if perm[0] > perm[1] or perm[1] > perm[2]:
                    continue
                if perm[1] - perm[0] == perm[2] - perm[1]:
                    return int(''.join(map(str, perm[:3])))


def run():
    print(answer())


class Test49(unittest.TestCase):
    def test_expected(self):
        expected = 296962999629
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

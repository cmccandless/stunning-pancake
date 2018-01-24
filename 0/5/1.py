#!/usr/bin/env python
# https://projecteuler.net/problem=51
import unittest
from itertools import combinations


def sieve(limit=1000000):
    yield 2
    np = set()
    for x in range(3, limit, 2):
        if x in np:
            continue
        yield x
        for y in range(x + x, limit, x):
            np.add(y)


primes = list(sieve())
p_set = set(primes)


def answer(members=8):
    for p in primes:
        s_p = str(p)
        num_digits = len(s_p)
        for i in range(1, num_digits):
            for c in combinations(range(num_digits), i):
                family_count = members
                base_prime = None
                for d in '9876543210':
                    if 0 in c and d == '0':
                        continue
                    new_n = int(''.join(
                        d if j in c else ch for j, ch in enumerate(s_p)
                    ))
                    if new_n in p_set:
                        family_count -= 1
                        base_prime = new_n
                        if family_count == 0:
                            return base_prime
                    # Not enough remaining members to check, so move on
                    elif family_count > int(d) + 1:
                        break


def run():
    # print(answer(6))  # 13
    # print(answer(7))  # 56003
    print(answer())


class Test51(unittest.TestCase):
    def test_expected(self):
        expected = 121313
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

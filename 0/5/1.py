#!/usr/bin/env python
# https://projecteuler.net/problem=51
import unittest
from itertools import combinations


def answer(members=8):
    limit = 1000000
    np = set()
    for x in range(3, limit, 2):
        if x in np:
            continue
        for y in range(x + x, limit, x):
            np.add(y)
    for p in range(3, limit, 2):
        if p in np:
            continue
        s_p = str(p)
        num_digits = len(s_p) - 1
        for i in range(3, num_digits - 1):
            for c in combinations(range(num_digits), i):
                family_count = members
                base_prime = None
                new_n = inc = 0
                for j, d in enumerate(s_p):
                    new_n *= 10
                    inc *= 10
                    if j in c:
                        new_n += 9
                        inc += 1
                    else:
                        new_n += int(d)
                for d in range(10, 1 if 0 in c else 0, -1):
                    if new_n & 1 and new_n not in np:
                        family_count -= 1
                        base_prime = new_n
                        if family_count == 0:
                            return base_prime
                    # Not enough remaining members to check, so move on
                    elif family_count > d:
                        break
                    new_n -= inc


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

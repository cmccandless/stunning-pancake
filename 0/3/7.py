#!/usr/bin/env python
# https://projecteuler.net/problem=37
import unittest


def answer(limit=1000000):
    total = 0
    not_prime = {1}
    for x in [3, 5, 7]:
        for y in range(x + x, limit, x):
            not_prime.add(y)
    for x in range(11, limit, 2):
        if x in not_prime:
            continue
        p, c = divmod(x, 10)
        pow10 = 0
        while (
            p & c & 1 and
            p not in not_prime and
            c not in not_prime
        ):
            pow10 += 1
            p, q = divmod(p, 10)
            c = q * pow(10, pow10) + c
        if (p == 0 or p == 2) and c not in not_prime:
            total += x
        for y in range(x + x, limit, x):
            not_prime.add(y)
    return total


def run():
    print(answer())


class Test37(unittest.TestCase):
    def test_expected(self):
        expected = 748317
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

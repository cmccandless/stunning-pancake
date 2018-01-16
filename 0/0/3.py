#!/usr/bin/env python
# https://projecteuler.net/problem=3
import unittest
from math import sqrt


def highest_prime_factor_under(target):
    notPrime = set()
    result = 1
    limit = round(sqrt(target))
    for i in range(2, limit):
        if i in notPrime:
            continue
        if target % i == 0:
            result = i
        for j in range(i, limit, i):
            notPrime.add(j)
    return result


def answer():
    return highest_prime_factor_under(600851475143)


def run():
    print(answer())


class Test3(unittest.TestCase):
    def test_expected(self):
        with open('../../answers.txt') as f:
            expected = int(f.readlines()[3])
        # expected = 6857
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

#!/usr/bin/env python
# https://projecteuler.net/problem=66
# Discussion: https://projecteuler.net/thread=66
from __future__ import division
import unittest
from math import sqrt


# Author: Kristian
# http://www.mathblog.dk/project-euler-66-diophantine-equation/
def answer(limit=1000):
    result = pmax = 0
    for D in range(2, limit + 1):
        limit = int(sqrt(D))
        if limit * limit == D:
            continue
        m, d, a = (0, 1, limit)
        numm1, num = (1, a)
        denm1, den = (0, 1)
        while num * num - D * den * den != 1:
            m = d * a - m
            d = (D - m * m) // d
            a = (limit + m) // d
            numm2, numm1 = (numm1, num)
            denm2, denm1 = (denm1, den)
            num, den = (a * numm1 + numm2, a * denm1 + denm2)
        if num > pmax:
            pmax, result = (num, D)
    return result


def run():
    assert answer(7) == 5
    print(answer())


class Test66(unittest.TestCase):
    def test_expected(self):
        expected = 661
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

#!/usr/bin/env python
# https://projecteuler.net/problem=73
# Discussion: https://projecteuler.net/thread=73
import unittest


# Author: kmmbvnr
# Runtime: 0.17s
# Source: https://projecteuler.net/thread=73;page=4#18116
def calc_less_than(x, n):
    # a[q] - number irreducible fractions less than x with
    # denominator equal to q
    n += 1
    a = [int(q * x) for q in range(n)]
    for q in range(1, n):
        m = 2
        mq = m * q
        while mq < n:
            a[mq] -= a[q]
            mq += q
    return sum(a) - 1


def answer(limit=12000):
    # Author: cmccandless
    # Runtime: 3.78s
    # count, start, stop = 0, 3, 2
    # s = [(start, stop)]
    # while s:
    #     b, d = s.pop()
    #     n = b + d
    #     if n > limit:
    #         continue
    #     count += 1
    #     s.append((b, n))
    #     s.append((n, d))
    # return count

    return calc_less_than(0.5, limit) - calc_less_than(1 / 3, limit) - 1


def run():
    print(answer())


class Test73(unittest.TestCase):
    def test_expected(self):
        expected = 7295372
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

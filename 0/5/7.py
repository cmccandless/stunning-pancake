#!/usr/bin/env python
# https://projecteuler.net/problem=57
# Discussion: https://projecteuler.net/thread=57
import unittest


def answer(limit=1000):
    # Author: cmccandless
    # Runtime: 0.16s
    count = 0
    n, d = (1, 2)
    for _ in range(limit):
        if len(str(n + d)) > len(str(d)):
            count += 1
        n, d = (d, 2 * d + n)
    return count

    # Author: KermitDFrog
    # https://projecteuler.net/thread=57;post=1773
    # Runtime: 0.15s
    # return 2 * (limit - 1) // 13


def run():
    print(answer())


class Test57(unittest.TestCase):
    def test_expected(self):
        expected = 153
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

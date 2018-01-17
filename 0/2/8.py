#!/usr/bin/env python
# https://projecteuler.net/problem=28
import unittest


def corners(n):
    x = n * n
    yield x
    if n > 1:
        for _ in range(3):
            x -= n - 1
            yield x


def answer(n=1001):
    return sum(x for i in range(1, n + 1, 2) for x in corners(i))


def run():
    # print(answer(5))  # 101
    print(answer())


class Test28(unittest.TestCase):
    def test_expected(self):
        expected = 669171001
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

#!/usr/bin/env python
# https://projecteuler.net/problem=6
import unittest


def square_of_sum(n):
    x = sum(range(1, n + 1))
    return x * x


def sum_of_squares(n):
    return sum([x * x for x in range(1, n + 1)])


def difference(n):
    return square_of_sum(n) - sum_of_squares(n)


def answer():
    return difference(100)


def run():
    print(answer())


class Test6(unittest.TestCase):
    def test_expected(self):
        expected = 25164150
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

#!/usr/bin/env python
# https://projecteuler.net/problem=65
# Discussion: https://projecteuler.net/thread=65
from __future__ import division
import unittest
from fractions import Fraction
from functools import reduce


def answer():
    return sum(
        ord(x) - 48
        for x in str(
            reduce(
                lambda f, x: x + Fraction(1, f),
                (
                    x
                    for k in range(33, -1, -1)
                    for x in (
                        (2,) if k == 0
                        else (1, 2 * k, 1)
                    )
                )
            ).numerator
        )
    )


def run():
    print(answer())


class Test65(unittest.TestCase):
    def test_expected(self):
        expected = 272
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

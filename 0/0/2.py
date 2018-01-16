#!/usr/bin/env python
# https://projecteuler.net/problem=2
import unittest
from itertools import takewhile


def fibon():
    a = 1
    b = 2
    yield a
    yield b
    while True:
        c = a + b
        yield c
        a = b
        b = c


def answer():
    limit = 4000000
    return sum(filter(
        lambda x: x % 2 == 0,
        takewhile(
            lambda x: x < limit,
            fibon()
        )
    ))


def run():
    print(answer())


class Test2(unittest.TestCase):
    def test_expected(self):
        with open('../../answers.txt') as f:
            expected = int(f.readlines()[2])
        # expected = 4613732
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

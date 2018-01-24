#!/usr/bin/env python
# https://projecteuler.net/problem=25
import unittest


def fibon():
    a = 1
    b = 1
    yield 0
    yield a
    yield b
    while True:
        c = a + b
        yield c
        a = b
        b = c


def answer(ndigits=1000):
    f = enumerate(fibon())
    index, x = next(f)
    while len(str(x)) < ndigits:
        index, x = next(f)
    return index


def run():
    # print(answer(3))
    print(answer())


class Test25(unittest.TestCase):
    def test_expected(self):
        expected = 4782
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

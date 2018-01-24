#!/usr/bin/env python
# https://projecteuler.net/problem=29
import unittest


def answer(limit=100):
    def combos(limit=limit):
        for a in range(2, limit + 1):
            x = a
            for _ in range(2, limit + 1):
                x *= a
                yield x
    return len(set(combos()))


def run():
    print(answer())


class Test29(unittest.TestCase):
    def test_expected(self):
        expected = 9183
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

#!/usr/bin/env python
# https://projecteuler.net/problem=62
# Discussion: https://projecteuler.net/thread=62
import unittest


def answer():
    counts = dict()
    n = 1
    while True:
        n += 1
        c = n * n * n
        s = ''.join(sorted(str(c)))
        prior, smallest_cube = counts.get(s, (0, c))
        if prior == 4:
            return smallest_cube
        else:
            counts[s] = (prior + 1, smallest_cube)


def run():
    print(answer())


class Test62(unittest.TestCase):
    def test_expected(self):
        expected = 127035954683
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

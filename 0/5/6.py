#!/usr/bin/env python
# https://projecteuler.net/problem=56
# Discussion: https://projecteuler.net/thread=56
import unittest


def answer():
    return max(
        sum(map(int, str(pow(a, b))))
        for a in range(1, 100)
        for b in range(1, 100)
    )


def run():
    print(answer())


class Test56(unittest.TestCase):
    def test_expected(self):
        expected = 972
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

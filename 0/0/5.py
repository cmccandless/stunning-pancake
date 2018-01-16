#!/usr/bin/env python
# https://projecteuler.net/problem=5
import unittest


def smallest_divisible(max, min=1):
    i = max
    while True:
        if all(i % x == 0 for x in range(min, max + 1)):
            return i
        i += max


def answer():
    return smallest_divisible(20)


def run():
    print(answer())


class Test5(unittest.TestCase):
    def test_expected(self):
        with open('../../answers.txt') as f:
            expected = int(f.readlines()[5])
        # expected = 232792560
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

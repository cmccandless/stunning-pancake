#!/usr/bin/env python
# https://projecteuler.net/problem=14
import unittest


def answer():
    limit = 1000000
    collatz = {1: 0}
    for i in range(2, limit):
        x = i
        chain = 1
        while x != 1:
            if x in collatz:
                chain += collatz[x] - 1
                break
            chain += 1
            if x % 2 == 0:
                x = x // 2
            else:
                x = 3 * x + 1
        collatz[i] = chain
    return max(
            collatz.items(),
            key=lambda t: t[1]
    )[0]


def run():
    print(answer())


class Test14(unittest.TestCase):
    def test_expected(self):
        with open('../../answers.txt') as f:
            expected = int(f.readlines()[14])
        # expected = 837799
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

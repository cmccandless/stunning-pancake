#!/usr/bin/env python
# https://projecteuler.net/problem=14
import unittest


def answer(limit=1000000):
    collatz = {1: 0}
    longest = 2
    longest_chain = 1
    for i in range(3, limit, 2):
        x = (3 * i + 1) >> 1
        chain = 3
        while True:
            if x & 1:
                if x < i:
                    break
                x = 3 * x + 1
                chain += 1
            x >>= 1
            chain += 1
        chain += collatz[x]
        collatz[i] = chain
        if chain > longest_chain:
            longest_chain = chain
            longest = i
    return longest


def run():
    print(answer())


class Test14(unittest.TestCase):
    def test_expected(self):
        expected = 837799
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

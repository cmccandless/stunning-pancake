#!/usr/bin/env python
# https://projecteuler.net/problem=22
import unittest
import os


try:
    fname = os.path.join('data', 'p022_names.txt')
    with open(fname):
        pass
except OSError:
    fname = os.path.join('..', '..', fname)


def score(word):
    return sum(ord(ch) - ord('A') + 1 for ch in word)


def answer():
    with open(fname) as f:
        names = sorted([n.strip('"') for n in f.read().split(',')])
    return sum(score(name) * (i + 1) for i, name in enumerate(names))


def run():
    # print(score('COLIN'))
    print(answer())


class Test22(unittest.TestCase):
    def test_expected(self):
        expected = 871198282
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

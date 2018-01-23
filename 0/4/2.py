#!/usr/bin/env python
# https://projecteuler.net/problem=42
import unittest
import os


try:
    fname = os.path.join('data', 'p042_words.txt')
    with open(fname):
        pass
except OSError:
    fname = os.path.join('..', '..', fname)


def score(word):
    return sum(ord(ch) - ord('@') for ch in word)


def answer():
    triangle_numbers = {n * (n + 1) // 2 for n in range(100)}
    with open(fname) as f:
        data = f.read()
    triangle_words = (
        1
        for w in (w.strip('"') for w in data.split(','))
        if score(w) in triangle_numbers
    )
    return sum(triangle_words)


def run():
    print(answer())


class Test42(unittest.TestCase):
    def test_expected(self):
        expected = 162
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

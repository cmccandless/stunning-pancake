#!/usr/bin/env python
# https://projecteuler.net/problem=59
# Discussion: https://projecteuler.net/thread=59
import unittest
from itertools import (
    combinations_with_replacement,
    cycle,
    permutations
)

import os
import sys
if sys.version_info[0] < 3:
    FILE_NOT_FOUND = IOError
else:
    FILE_NOT_FOUND = OSError

try:
    fname = os.path.join('data', 'p059_cipher.txt')
    with open(fname):
        pass
except FILE_NOT_FOUND:
    fname = os.path.join('..', '..', fname)


def answer():
    with open(fname) as f:
        chars = [int(n) for n in f.read().split(',')]
    # solution = (103, 111, 100)
    letters = range(ord('a'), ord('z') + 1)
    for combo_key in combinations_with_replacement(letters, 3):
        for key in permutations(combo_key):
            codes = [x ^ y for x, y in zip(chars, cycle(key))]
            decoded = ''.join(map(chr, codes))
            if 'the' in decoded and 'this' in decoded:
                return sum(codes)


def run():
    print(answer())


class Test59(unittest.TestCase):
    def test_expected(self):
        expected = 107359
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

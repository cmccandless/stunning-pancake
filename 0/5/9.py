#!/usr/bin/env python
# https://projecteuler.net/problem=59
# Discussion: https://projecteuler.net/thread=59
import unittest
from itertools import cycle

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


def keys(size=3, min_char='a', max_char='z'):
    min_ord = ord(min_char)
    max_ord = ord(max_char)
    start = [min_ord] * size
    stop = [max_ord] * size
    while start != stop:
        yield tuple(start)
        i = -1
        start[i] += 1
        while start[i] > max_ord:
            start[i] = min_ord
            i -= 1
            start[i] += 1
    yield tuple(start)


def answer():
    with open(fname) as f:
        chars = [int(n) for n in f.read().split(',')]
    for key in keys(3, 'a', 'z'):
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

#!/usr/bin/env python
# https://projecteuler.net/problem=67
# Discussion: https://projecteuler.net/thread=67
import unittest

import os
import sys
if sys.version_info[0] < 3:
    FILE_NOT_FOUND = IOError
else:
    FILE_NOT_FOUND = OSError

try:
    fname = os.path.join('data', 'p067_triangle.txt')
    with open(fname):
        pass
except FILE_NOT_FOUND:
    fname = os.path.join('..', '..', fname)


def answer():
    with open(fname) as f:
        data = [
            [int(x) for x in line.strip().split(' ')]
            for line in f.readlines()
        ]
    sums = list(data[0])
    for line in data[1:]:
        sums = (
            [sums[0] + line[0]] +
            [
                line[i] + max(sums[i - 1:i + 1])
                for i in range(1, len(line) - 1)
            ] +
            [sums[-1] + line[-1]]
        )
    return max(sums)


def run():
    print(answer())


class Test67(unittest.TestCase):
    def test_expected(self):
        expected = 7273
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

#!/usr/bin/env python
# https://projecteuler.net/problem=68
# Discussion: https://projecteuler.net/thread=68
import unittest
from itertools import permutations


def answer(ring_size=5, target_digits=16):
    limit = 2 * ring_size
    nums = set(range(1, limit + 1))
    for outer in permutations(range(limit, 0, -1), ring_size):
        if limit not in outer or min(outer) != outer[0]:
            continue
        for inner in map(list, permutations(nums.difference(outer))):
            slices = [
                [o, inner[j - 1], inner[j]]
                for j, o in enumerate(outer)
            ]
            total = sum(map(sum, slices)) // ring_size
            if all(total == sum(s) for s in slices):
                return int(
                    ''.join(
                        ''.join(map(str, s))
                        for s in slices
                    )
                )


def run():
    # print(answer(3, 9))
    print(answer())


class Test68(unittest.TestCase):
    def test_expected(self):
        expected = 6531031914842725
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

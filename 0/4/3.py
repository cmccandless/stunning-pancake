#!/usr/bin/env python
# https://projecteuler.net/problem=43
import unittest
from itertools import permutations


def answer():
    divisors = [2, 3, 5, 7, 11, 13, 17]
    total = 0
    digits = '0123456789'
    s = [(''.join(p), divisors[0:]) for p in permutations(digits, 3)]
    while s:
        used, divisors = s.pop()
        divisor = divisors.pop(0)
        for d in digits:
            if d in used or int(used[-2:] + d) % divisor != 0:
                continue
            if divisors:
                s.append((used + d, divisors[0:]))
            else:
                total += int(used + d)
    return total


def run():
    print(answer())


class Test43(unittest.TestCase):
    def test_expected(self):
        expected = 16695334890
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

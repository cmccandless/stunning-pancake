#!/usr/bin/env python
# https://projecteuler.net/problem=4
import unittest


def is_palindrome(num):
    return str(num) == str(num)[-1::]


def largest_palindrom_product(digits):
    min_factor = pow(10, digits - 1)
    max_factor = min_factor * 10 - 1
    best = (min_factor * min_factor, {min_factor})
    for m in reversed(range(min_factor, max_factor + 1)):
        for n in reversed(range(min_factor, m + 1)):
            p = m * n
            s = str(p)
            if s == s[::-1]:
                if best[0] < p:
                    best = (p, {m, n})
                continue
    return best


def answer():
    return largest_palindrom_product(2)[0]


def run():
    print(answer())


class Test4(unittest.TestCase):
    def test_expected(self):
        with open('../../answers.txt') as f:
            expected = int(f.readlines()[4])
        # expected = 9009
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

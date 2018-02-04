#!/usr/bin/env python
# https://projecteuler.net/problem=53
# Discussion: https://projecteuler.net/thread=53
import unittest


def answer():
    factorial = [1, 1]
    f = 1
    for n in range(2, 101):
        f *= n
        factorial.append(f)
    count = 0
    for n in range(1, 101):
        fn = factorial[n]
        for r in range(n // 2):
            ncr = fn / (factorial[r] * factorial[n - r])
            if ncr > 1000000:
                count += n - r - r + 1
                break
    return count


def run():
    print(answer())


class Test53(unittest.TestCase):
    def test_expected(self):
        expected = 4075
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

#!/usr/bin/env python
# https://projecteuler.net/problem=39
import unittest


def answer(limit=1000):
    best = count = 0
    for p in range(12, limit + 1, 2):
        local_count = 0
        for a in range(2, limit // 2, 2):
            a_squared = a * a
            b = a
            c = p - a - b
            while b < c:
                if a_squared + b * b == c * c:
                    local_count += 1
                b += 2
                c -= 2
        if local_count > count:
            best = p
            count = local_count
    return best


def run():
    print(answer())


class Test39(unittest.TestCase):
    def test_expected(self):
        expected = 840
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

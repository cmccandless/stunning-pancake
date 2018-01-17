#!/usr/bin/env python
# https://projecteuler.net/problem=30
import unittest


def match(num, power):
    return sum(pow(int(d), power) for d in str(num)) == num


def answer(power=5):
    return sum(
        x for x in range(2, 195000)
        if match(x, power)
    )


def run():
    # print(answer(4))
    print(answer())


class Test30(unittest.TestCase):
    def test_expected(self):
        expected = 443839
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

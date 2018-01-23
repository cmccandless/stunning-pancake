#!/usr/bin/env python
# https://projecteuler.net/problem=48
import unittest


def modexp(g, u, p):
    s = 1
    while u != 0:
        if u & 1:
            s = (s * g) % p
        u >>= 1
        g = (g * g) % p
    return s


def answer(num=1000):
    limit = pow(10, 10)
    return sum(modexp(n, n, limit) for n in range(1, num + 1)) % limit


def run():
    # print(answer(10))
    print(answer())


class Test48(unittest.TestCase):
    def test_expected(self):
        expected = 9110846700
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

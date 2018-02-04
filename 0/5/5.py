#!/usr/bin/env python
# https://projecteuler.net/problem=55
# Discussion: https://projecteuler.net/thread=55
import unittest


def answer(limit=10000):
    count = 0
    for i in range(1, limit):
        x = int(str(i)[::-1]) + i
        sx = str(x)
        rsx = sx[::-1]
        lychrel = True
        for j in range(1, 50):
            if sx == sx[::-1]:
                lychrel = False
                break
            x += int(rsx)
            sx = str(x)
            rsx = sx[::-1]
        if lychrel:
            count += 1
    return count


def run():
    print(answer())


class Test55(unittest.TestCase):
    def test_expected(self):
        expected = 249
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

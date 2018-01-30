#!/usr/bin/env python
# https://projecteuler.net/problem=63
# Discussion: https://projecteuler.net/thread=63
import unittest


def answer():
    count = 0
    i = 0
    while True:
        i += 1
        n = 1
        while len(str(pow(n, i))) < i:
            n += 1
        if len(str(pow(n, i))) > i:
            break
        while len(str(pow(n, i))) == i:
            count += 1
            n += 1
    return count


def run():
    print(answer())


class Test63(unittest.TestCase):
    def test_expected(self):
        expected = 49
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

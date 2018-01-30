#!/usr/bin/env python
# https://projecteuler.net/problem=61
# Discussion: https://projecteuler.net/thread=61
import unittest
from itertools import dropwhile, takewhile
from functools import reduce


def polygonal(f):
    yield 0
    yield 1
    n = 1
    while True:
        n += 1
        yield f(n)


def polygonal_e(f):
    return {
        x
        for x in takewhile(
            lambda x: x < 10000,
            dropwhile(
                lambda x: x < 1000,
                polygonal(f)
            )
        )
    }


def answer():
    p = [
        polygonal_e(lambda n: (n * (n + 1)) // 2),
        polygonal_e(lambda n: n * n),
        polygonal_e(lambda n: (n * (3 * n - 1)) // 2),
        polygonal_e(lambda n: n * (2 * n - 1)),
        polygonal_e(lambda n: (n * (5 * n - 3)) // 2),
        polygonal_e(lambda n: n * (3 * n - 2))
    ]
    s = [
        ([x], {j for j in range(6) if i != j})
        for i, poly in enumerate(p)
        for x in poly
    ]
    while s:
        c, unused = s.pop()
        if unused:
            for i in unused:
                for n in p[i]:
                    if n in c:
                        continue
                    if str(c[-1])[-2:] == str(n)[:2]:
                        new_chain = c + [n]
                        new_used = unused.difference([i])
                        s.append((new_chain, new_used))
        elif str(c[-1])[-2:] == str(c[0])[:2]:
            return sum(c)


def run():
    print(answer())


class Test61(unittest.TestCase):
    def test_expected(self):
        expected = 28684
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

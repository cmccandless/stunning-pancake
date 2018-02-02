#!/usr/bin/env python
# https://projecteuler.net/problem=74
# Discussion: https://projecteuler.net/thread=74
import unittest
from itertools import (
    combinations_with_replacement,
    permutations,
)


def answer(limit=1000000, target=60):
    factorial = [1, 1]
    for i in range(2, 10):
        factorial.append(i * factorial[-1])

    def get_next_link(n):
        y = 0
        while n != 0:
            n, r = divmod(n, 10)
            y += factorial[r]
        return y

    count = 0
    for num_digits in range(1, 7):
        for digits in combinations_with_replacement(range(0, 10), num_digits):
            s = sum(
                factorial[d]
                for d in digits
            )
            links = {s}
            y = get_next_link(s)
            while y not in links:
                links.add(y)
                y = get_next_link(y)
            chain = len(links) + 1
            if chain == target:
                perms = len({
                    p for p in permutations(digits)
                    if p[0] != 0
                })
                count += perms
    return count


def run():
    print(answer())


class Test74(unittest.TestCase):
    def test_expected(self):
        expected = 402
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

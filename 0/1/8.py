#!/usr/bin/env python
# https://projecteuler.net/problem=18
import unittest

sample_data = """3
7 4
2 4 6
8 5 9 3"""
sample_data = [
    [int(n) for n in line.split(' ')]
    for line in sample_data.split('\n')
]

__data__ = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
__data__ = [
    [int(n) for n in line.split(' ')]
    for line in __data__.split('\n')
]


def answer(data=__data__):
    sums = list(data[0])
    for line in data[1:]:
        sums = (
            [sums[0] + line[0]] +
            [
                line[i] + max(sums[i - 1:i + 1])
                for i in range(1, len(line) - 1)
            ] +
            [sums[-1] + line[-1]]
        )
    return max(sums)


def run():
    print(answer(sample_data))  # 23
    print(answer(__data__))


class Test18(unittest.TestCase):
    def test_expected(self):
        expected = 1074
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

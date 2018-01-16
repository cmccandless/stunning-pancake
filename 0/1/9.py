#!/usr/bin/env python
# https://projecteuler.net/problem=19
import unittest


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days(month, year):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in {9, 4, 6, 11}:
        return 30
    else:
        return 31


def step(year, month, day, day_of_week):
    dm, day = divmod(day, days(month, year))
    day += 1
    dy, month = divmod(month + dm - 1, 12)
    month += 1
    return (year + dy, month, day, (day_of_week + 1) % 7)


def answer(start_year=1901, stop_year=2001, count_day=1, count_day_of_week=0):
    month = 1
    year = 1900
    day = 1
    day_of_week = 1
    data = (year, month, day, day_of_week)
    while data[0] < start_year:
        data = step(*data)
    count = 0
    while data[0] < stop_year:
        if data[2] == count_day and data[3] == count_day_of_week:
            count += 1
        data = step(*data)
    return count


def run():
    print(answer())


class Test19(unittest.TestCase):
    def test_step_1900_1_1_1(self):
        self.assertEqual(step(1900, 1, 1, 1), (1900, 1, 2, 2))

    def test_step_1900_1_1_30_2(self):
        self.assertEqual(step(1900, 1, 30, 2), (1900, 1, 31, 3))

    def test_step_1900_1_1_31_3(self):
        self.assertEqual(step(1900, 1, 31, 3), (1900, 2, 1, 4))

    def test_step_1900_2_28_2(self):
        self.assertEqual(step(1900, 2, 28, 2), (1900, 3, 1, 3))

    def test_step_1901_2_28_2(self):
        self.assertEqual(step(1901, 2, 28, 2), (1901, 3, 1, 3))

    def test_step_1904_2_28_2(self):
        self.assertEqual(step(1904, 2, 28, 2), (1904, 2, 29, 3))

    def test_step_1900_12_31_6(self):
        self.assertEqual(step(1900, 12, 31, 6), (1901, 1, 1, 0))

    def test_expected(self):
        with open('../../answers.txt') as f:
            expected = int(f.readlines()[19])
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

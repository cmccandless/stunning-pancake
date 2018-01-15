#!/usr/bin/env python


def square_of_sum(n):
    x = sum(range(1, n + 1))
    return x * x


def sum_of_squares(n):
    return sum([x * x for x in range(1, n + 1)])


def difference(n):
    return square_of_sum(n) - sum_of_squares(n)


def run():
    print(difference(100))
    

if __name__ == '__main__':
    run()

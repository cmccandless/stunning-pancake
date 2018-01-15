#!/usr/bin/env python
# https://projecteuler.net/problem=1


def mults_of(n, under):
    return {x for x in range(n, under, n)}


def run():
    under = 1000
    print(sum(mults_of(3, under).union(mults_of(5, under))))


if __name__ == '__main__':
    run()

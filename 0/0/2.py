#!/usr/bin/env python
# https://projecteuler.net/problem=2


from itertools import takewhile


def fibon():
    a = 1
    b = 2
    yield a
    yield b
    while True:
        c = a + b
        yield c
        a = b
        b = c


def run():
    limit = 4000000
    print(sum(filter(
        lambda x: x % 2 == 0,
        takewhile(
            lambda x: x < limit,
            fibon()
        )
    )))


if __name__ == '__main__':
    run()

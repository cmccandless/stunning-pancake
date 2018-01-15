#!/usr/bin/env python
# https://projecteuler.net/problem=9


from math import sqrt


def is_triplet(a, b, c):
    return a * a + b * b == c * c


def run():
    target = 1000
    limit = 10000
    for a in range(1, limit):
        for b in range(1, a):
            c = int(sqrt(a * a + b * b))
            if a + b + c == target:
                print(a * b * c)
                return
    print('fail')    


if __name__ == '__main__':
    run()

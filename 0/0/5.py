#!/usr/bin/env python


def smallest_divisible(max, min=1):
    i = max
    while True:
        if all(i % x == 0 for x in range(min, max + 1)):
            return i
        i += max


def run():
    print(smallest_divisible(20))
    

if __name__ == '__main__':
    run()

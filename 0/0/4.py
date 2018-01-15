#!/usr/bin/env python


def is_palindrome(num):
    return str(num) == str(num)[-1::]


def largest_palindrom_product(digits):
    min_factor = pow(10, digits - 1)
    max_factor = min_factor * 10 - 1
    best = (min_factor * min_factor, {min_factor})
    for m in reversed(range(min_factor, max_factor + 1)):
        for n in reversed(range(min_factor, m + 1)):
            p = m * n
            s = str(p)
            if s == s[::-1]:
                if best[0] < p:
                    best = (p, {m, n})
                continue
    return best


def run():
    print(largest_palindrom_product(2))[0]
    

if __name__ == '__main__':
    run()

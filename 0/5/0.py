#!/usr/bin/env python
# https://projecteuler.net/problem=50
import unittest


def sieve(limit=1000000):
    yield 2
    np = set()
    for x in range(3, limit, 2):
        if x in np:
            continue
        yield x
        for y in range(x + x, limit, x):
            np.add(y)


def answer(limit=1000000):
    primes = list(sieve(limit))
    p_set = set(primes)
    length = longest_sum = 0
    candidates = []
    for p in primes:
        to_remove = []
        for i in range(len(candidates)):
            total, count = candidates[i]
            total += p
            count += 1
            if total < limit:
                candidates[i] = (total, count)
                if count > length and total in p_set:
                    longest_sum, length = (total, count)
            else:
                to_remove.append(i)
        for i in reversed(to_remove):
            del candidates[i]
        candidates.append((p, 1))
    return longest_sum


def run():
    # print(answer(100))  # 41
    # print(answer(1000))  # 953
    print(answer())


class Test50(unittest.TestCase):
    def test_expected(self):
        expected = 997651
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

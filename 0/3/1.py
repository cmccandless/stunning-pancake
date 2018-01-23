#!/usr/bin/env python
# https://projecteuler.net/problem=31
import unittest


class HashableDict(dict):
    def __hash__(self):
        return hash(tuple(sorted(self.items())))


def add_coin(combo, coin):
    combo = HashableDict(combo)
    combo[coin] = combo.get(coin, 0) + 1
    return combo


def answer(target=200, coins=[1, 2, 5, 10, 20, 50, 100, 200]):
    # Author: cmccandless
    # Runtime: ~33s
    # counts = [set() for _ in range(target + 1)]
    # for i in range(1, len(counts)):
    #     for c in coins:
    #         if c == i:
    #             ns = HashableDict({c: 1})
    #             counts[i].add(ns)
    #         elif c > i:
    #             j = i - c
    #             for s in counts[j]:
    #                 counts[i].add(add_coin(s, c))
    # return len(counts[target])

    # Faster solution
    # Author: grimbal
    # Source: https://projecteuler.net/thread=31#411
    # Runtime: ~0.278s
    # count = 0
    # for a in range(target, -1, -200):
    #     for b in range(a, -1, -100):
    #         for c in range(b, -1, -50):
    #             for d in range(c, -1, -20):
    #                 for e in range(d, -1, -10):
    #                     for f in range(e, -1, -5):
    #                         for g in range(f, -1, -2):
    #                             count += 1
    # return count

    # Recursive interpretation
    # Author: cmccandless
    # Runtime: ~0.326s
    # if len(coins) > 1:
    #     coins = list(coins)
    #     coin = coins.pop()
    #     return sum(
    #         answer(x, coins)
    #         for x in range(target, -1, -coin)
    #     )
    # elif len(coins) == 1 and target % coins[0] == 0:
    #     return 1
    # else:
    #     return 0

    # Optimized iterative solution for any coin set
    # Author: cmccandless
    # Runtime: ~0.343s
    stack = [(target, list(coins))]
    count = 0
    while stack:
        target, coins = stack.pop()
        coin = coins.pop()
        if coins:
            for x in range(target, -1, -coin):
                stack.append((x, list(coins)))
        else:
            if target % coin == 0:
                count += 1
    return count


def run():
    print(answer())


class Test31(unittest.TestCase):
    def test_expected(self):
        expected = 73682
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

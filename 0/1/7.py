#!/usr/bin/env python
# https://projecteuler.net/problem=17
import unittest

d = ['', 'one', 'two', 'three', 'four', 'five', 'six',
     'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
     'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
     'eighteen', 'nineteen']
tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty',
        'sixty', 'seventy', 'eighty', 'ninety']
label = ['hundred', 'thousand', 'million', 'billion']


def say(n):
    if n < 0:
        raise ValueError('cannot say negative numbers')
    if n >= 1000000000000:
        raise ValueError('cannot say numbers greater than or equal to 1T')
    elif n == 0:
        return 'zero'
    s = str(int(n))
    lenS = len(s)
    t = [(max(0, lenS - 3 - i), lenS - i) for i in range(0, lenS, 3)]
    t2 = [(i, j[0], j[1]) for i, j in enumerate(t)]
    parts = [(int(float(s[x:y])), i) for i, x, y in t2]
    result = ''
    for value, ex in [x for x in parts if x[0] > 0]:
        if ex > 0:
            result = ' '.join([say(value), label[ex], result])
            continue
        under = value % 100
        if under == 0:
            result = ' '.join([d[int(value / 100)], label[ex]])
            continue
        if under < 20:
            underStr = d[under]
        elif under % 10 == 0:
            underStr = tens[int(under / 10)]
        else:
            underStr = '-'.join([tens[int(under / 10)], d[under % 10]])
        if value > 99:
            result = ' '.join([d[int(value / 100)],
                               label[ex],
                               'and',
                               underStr])
        else:
            if len(parts) > 1:
                underStr = ' '.join(['and', underStr])
            result = underStr
    return result.replace('  ', ' ').strip()


def answer(count=1000):
    return sum(
        len([ch for ch in say(i) if ch not in ' -'])
        for i in range(1, count + 1)
    )


def run():
    # print(answer(5))
    print(answer())


class Test17(unittest.TestCase):
    def test_expected(self):
        with open('../../answers.txt') as f:
            expected = int(f.readlines()[17])
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()

#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        from latest import latest
        exercise = str(int(latest()) + 1)
    else:
        exercise = sys.argv[1]
    exercise = exercise.rjust(3, '0')
    dpath = os.path.join(*exercise[:-1])
    if not os.path.isdir(dpath):
        os.makedirs(dpath)

    with open(os.path.join(*exercise) + '.py', 'w') as f:
        f.write("""#!/usr/bin/env python
# https://projecteuler.net/problem={0}
# Discussion: https://projecteuler.net/thread={0}
import unittest


def answer():
    pass


def run():
    print(answer())


class Test{0}(unittest.TestCase):
    def test_expected(self):
        expected = 'FILL IN ANSWER ONCE ACCEPTED'
        self.assertEqual(answer(), expected)


if __name__ == '__main__':
    run()
""".format(int(exercise)))

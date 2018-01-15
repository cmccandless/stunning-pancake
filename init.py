#!/usr/bin/env python
import os
import sys

exercise = sys.argv[1].rjust(3, '0')
dpath = os.path.join(*exercise[:-1])
if not os.path.isdir(dpath):
    os.makedirs(dpath)

with open(os.path.join(*exercise) + '.py', 'w') as f:
    f.write("""#!/usr/bin/env python
# https://projecteuler.net/problem={}


def run():
    pass


if __name__ == '__main__':
    run()
""".format(int(exercise)))

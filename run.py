#!/usr/bin/env python
from importlib import import_module
import sys


if __name__ == '__main__':
    if len(sys.argv) < 2:
        from latest import latest
        exercise = str(int(latest()))
    else:
        exercise = sys.argv[1]
    exercise = exercise.rjust(3, '0')
    module = import_module('{}.{}.{}'.format(*exercise))
    getattr(module, 'run')()

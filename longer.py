#!/usr/bin/env python
from __future__ import print_function
import sys
import re

try:
    limit = float(sys.argv[1])
except IndexError:
    limit = 1.0

rgxTest = re.compile('.*Test(\d+).*(PASSED|FAILED)')
rgxTime = re.compile('.*(\d+\.\d+) seconds.*')

ret_OK = True

try:
    lines = iter(sys.stdin)
    while True:
        line = next(lines)
        m = rgxTest.match(line)
        if m:
            testno = int(m.group(1))
            result = m.group(2)
            next(lines)  # Skip blank line
            line = next(lines)
            m = rgxTime.match(line)
            if m:
                time = m.group(1)
                OK = float(time) < limit
                if result == 'PASSED':
                    if not OK:
                        result = 'TOO_LONG'
                else:
                    OK = False
                print(
                    'Test{:03d}'.format(testno),
                    time,
                    'seconds',
                    result
                )
                ret_OK = ret_OK and OK
except StopIteration:
    pass

sys.exit(0 if ret_OK else 1)

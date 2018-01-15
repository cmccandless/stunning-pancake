#!/usr/bin/env python
import os
for i in range(0, 10):
    if os.path.isdir(str(i)):
        os.system('chmod +x {}/*/*.py'.format(i))

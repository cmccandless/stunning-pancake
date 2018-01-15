#!/usr/bin/env python
# import os
# import sys
from importlib import import_module
import sys

exercise = sys.argv[1].rjust(3, '0')
module = import_module('{}.{}.{}'.format(*exercise))
getattr(module, 'run')()

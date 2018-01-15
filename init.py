#!/usr/bin/env python
import os
import sys

exercise = sys.argv[1].rjust(3, '0')
os.makedirs(os.path.join(*exercise[:-1]))

with open(os.path.join(*exercise) + '.py', 'w') as f:
    f.write("""#!/usr/bin/env python
def run():
    pass


if __name__ == '__main__':
    run()
""")

import os


def latest():
    for i in range(10, -1, -1):
        if not os.path.isdir(str(i)):
            continue
        for j in range(10, -1, -1):
            if not os.path.isdir(
                os.path.join(str(i), str(j))
            ):
                continue
            for k in range(10, -1, -1):
                if os.path.isfile(
                    os.path.join(str(i), str(j), str(k) + '.py')
                ):
                    return ''.join(map(str, [i, j, k]))

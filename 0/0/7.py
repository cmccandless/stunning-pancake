def sieve(limit=1000000):
    notPrime = set()
    for x in range(2, limit):
        if x in notPrime:
            continue
        yield x
        for i in range(x, limit, x):
            notPrime.add(i)


def run():
    sieve_gen = sieve()
    for i in range(10001):
        x = next(sieve_gen)
    print(x)


if __name__ == '__main__':
    run()

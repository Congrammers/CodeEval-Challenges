import sys
from collections import OrderedDict
from itertools import tee, islice, chain

def now_and_next(some_iterable):
    items, nexts = tee(some_iterable, 2)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(items, nexts)

def brent(f, x0):
    power = lam = 1
    tortoise = x0
    hare = f(x0)
    while tortoise != hare:
        if power == lam:
            tortoise = hare
            power *= 2
            lam = 0
        hare = f(hare)
        lam += 1

    mu = 0
    tortoise = hare = x0
    for i in range(lam):
        hare = f(hare)

    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)
        mu += 1

    return lam, mu

def fetch(val):
    return funcTable[val]

def get_range(dictionary, begin, end):
    return list(islice(dictionary.keys(), begin, end+1))

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        line = line.rstrip().split()

        pairList = []
        for m, n in now_and_next(line):
            if not n:
                break
            pairList.append((m, n))
        funcTable = OrderedDict(pairList)
        lam, start = brent(fetch, list(funcTable.keys())[0])

        seqOrder = get_range(funcTable, start, len(funcTable))
        print(" ".join(seqOrder))

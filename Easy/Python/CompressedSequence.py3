import sys
from itertools import tee, islice, chain

def nowAndNext(iterable):
    items, nexts = tee(iterable, 2)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(items, nexts)

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        line = line.rstrip().split()

        result = []
        currentCount = 1
        for val, peek in nowAndNext(line):
            if val != peek:
                result.append(str(currentCount))
                result.append(val)
                val == peek
                currentCount = 0
            currentCount += 1

        print(" ".join(result))

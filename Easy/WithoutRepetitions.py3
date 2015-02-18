import sys
from itertools import tee, chain

def prev_and_now(some_iterable):
    items, prevs = tee(some_iterable, 2)
    prevs = chain([None], prevs)
    return zip(prevs, items)

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        line = line.rstrip().split()

        result = ""
        for word in line:
            for prevs, now in prev_and_now(list(word)):
                if prevs != now:
                    result += now
            result += ' '

        print(result)

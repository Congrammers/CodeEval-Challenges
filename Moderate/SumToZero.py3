import itertools
import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        line = list(map(int, line.rstrip().split(',')))

        cc = []
        optimizedLen = 5 if len(line)+1 >= 5 else len(line)+1
        for i in range(optimizedLen):
            for c in itertools.combinations(line, i):
                if len(c) == 4 and sum(c) == 0:
                    cc.append(c)
        print(len(cc))

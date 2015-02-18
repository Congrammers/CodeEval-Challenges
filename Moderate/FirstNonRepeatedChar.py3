import sys
from collections import Counter

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        line = list(line.rstrip())
        for c in line:
            if line.count(c) == 1:
                print(c)
                break

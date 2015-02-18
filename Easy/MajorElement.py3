import sys
from collections import Counter

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        line = line.rstrip().split(',')
        c = Counter(line)
        rules = len(line) / 2

        most = c.most_common()[0]
        result, mostCount = most
        result = result if mostCount > rules else None

        if result:
            print(result)
        else:
            print("None")

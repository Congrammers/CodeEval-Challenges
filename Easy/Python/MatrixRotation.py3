import sys
from math import sqrt

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        line = line.rstrip().split()
        root = int(sqrt(len(line)))

        matrixed = [[line[x+y*root] for x in range(root)]
                    for y in range(root)]
        rotated = list(zip(*matrixed[::-1]))

        result = []
        for y in range(root):
            for x in range(root):
                result.append(rotated[y][x])

        print(" ".join(result))

import itertools
import sys

def pascalTri(n):
    line = [1]
    for k in range(n):
        line.append(line[k] * (n-k) / (k+1))
    return line

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        depth = int(line.rstrip())

        result = []
        for n in range(depth):
            result.append(map(str, list(map(int, pascalTri(n)))))

        print(" ".join(list(itertools.chain.from_iterable(result))))

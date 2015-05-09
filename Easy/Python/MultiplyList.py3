import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        first, second = line.rstrip().split(' | ')
        first = list(map(int, first.split()))
        second = list(map(int, second.split()))
        result = [a * b for a, b in zip(first, second)]
        print(" ".join(map(str, result)))

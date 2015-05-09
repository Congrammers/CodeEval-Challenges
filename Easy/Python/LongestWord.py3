import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        print(max(line.rstrip().split(), key=len))

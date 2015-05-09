import sys

firstArgs = sys.argv[1]
with open(firstArgs, 'r') as inFile:
    for line in inFile:
        n, p1, p2 = map(int, line.rstrip().split(","))
        print(str.lower(str(((n >> (p1-1)) & 1) == ((n >> (p2-1)) & 1))))

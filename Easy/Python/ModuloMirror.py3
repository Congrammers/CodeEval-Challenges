import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        total, div = list(map(int, line.rstrip().split(",")))
        multi = int(total / div)
        remain = total - (div * multi)
        print(remain)

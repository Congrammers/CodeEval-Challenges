import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        line = line.rstrip().split()
        listing, pos = line[:-1], int(line[-1])
        if (pos <= len(listing)):
            print(listing[-pos])

import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        line = line.rstrip()
        print(bin(int(line))[2:])

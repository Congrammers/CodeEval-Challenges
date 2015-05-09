import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        hexa = line.rstrip()
        print(int(hexa, 16))

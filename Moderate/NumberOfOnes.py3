import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        line = line.rstrip()
        binary = bin(int(line))[2:]
        print(binary.count("1"))

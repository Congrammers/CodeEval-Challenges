import sys

firstArgs = sys.argv[1]
with open(firstArgs, 'r') as inFile:
    for line in inFile:
        print(str.lower(line.strip()))

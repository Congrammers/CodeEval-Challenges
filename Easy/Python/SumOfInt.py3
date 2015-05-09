import sys

firstArgs = sys.argv[1]
with open(firstArgs, 'r') as inFile:
    total = 0
    for line in inFile:
        total += int(line.rstrip())
    print(total)

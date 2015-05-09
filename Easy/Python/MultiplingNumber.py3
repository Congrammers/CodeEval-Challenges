import sys

firstArgs = sys.argv[1]
with open(firstArgs, 'r') as inFile:
    for line in inFile:
        roof, value = map(int, line.rstrip().split(","))
        counter = 1
        while counter:
            if roof <= value * counter:
                print(value * counter)
                break
            counter += 1

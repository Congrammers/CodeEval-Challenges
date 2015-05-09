import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        string, char = line.rstrip().split(",")
        if not char:
            print(-1)
            continue

        zeroBasedInversePos = (string[::-1].find(char))
        if (zeroBasedInversePos != -1):
            inversePos = zeroBasedInversePos + 1
            print(len(string) - inversePos)
        else:
            print(zeroBasedInversePos)

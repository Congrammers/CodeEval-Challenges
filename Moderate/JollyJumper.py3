import sys

def isJolly(a, genSet):
    valueList = list(map(lambda x, y: abs(x - y), a[1:], a[:-1]))
    generatedSet = [n+1 for n in range(genSet-1)]
    reversedSet = list(reversed(generatedSet))

    sanityTest = generatedSet == valueList or reversedSet == valueList
    return sanityTest

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        line = list(map(int, line.rstrip().split()))
        val = line[0]
        listing = line[1:]

        if isJolly(listing, val):
            print("Jolly")
        else:
            print("Not jolly")

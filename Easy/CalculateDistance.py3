import sys
from math import sqrt

def getPos(string):
    string = string.strip('()')
    x, y = map(int, string.split(', '))
    return [x, y]

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        first, second = line.rstrip().split(') (')
        first = getPos(first)
        second = getPos(second)

        a = (first[0] - second[0])
        b = (first[1] - second[1])
        c = sqrt(a**2 + b**2)
        print(int(c))

import sys

def swap(num, value):
    init, to = map(int, value.split('-'))
    num[init], num[to] = num[to], num[init]

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        number, splitter = line.rstrip().split(' : ')
        number = list(number.split())
        splitter = list(splitter.split(', '))

        for val in splitter:
            swap(number, val)
        print(" ".join(number))

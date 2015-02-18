from __future__ import print_function
import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        stack = line.rstrip().split()
        flipFlop = True

        while stack:
            val = stack.pop()
            if flipFlop:
                print(val, end=" ")
                flipFlop = False
            else:
                flipFlop = True
        print()

import sys
from math import sqrt

firstArgs = sys.argv[1]
with open(firstArgs, 'r') as inFile:
    for line in inFile:
        # Binet's Formula
        fibonacci = lambda n: (((1 + sqrt(5))**n) - ((1 - sqrt(5))**n))\
            / ((2**n) * sqrt(5))
        print(round(fibonacci(int(line.rstrip()))))

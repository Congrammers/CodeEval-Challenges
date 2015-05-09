import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        num = sorted(list(map(float, line.rstrip().split(" "))))
        num = ["{:.3f}".format(n) for n in num]
        print(" ".join(num))

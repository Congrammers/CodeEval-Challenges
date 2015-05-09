import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        print(",".join(map(str, sorted(
            set(map(int, list(line.rstrip().split(","))))))))

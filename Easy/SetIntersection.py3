import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        listPair = line.rstrip().split(";")
        first = map(int, listPair[0].split(","))
        second = map(int, listPair[1].split(","))

        print(",".join(map(str, sorted(
            set(first) & set(second)))))

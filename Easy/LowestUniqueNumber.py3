import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        number = list(map(int, line.rstrip().split()))
        unique = [n for n in number if number.count(n) == 1]

        if len(unique) == 0:
            print(0)
            continue

        print(number.index(min(unique)) + 1)

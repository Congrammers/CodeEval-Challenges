import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        if line in ['\n', '\r\n']:
            continue

        letterPile, position = list(line.rstrip().split("| "))
        letterPile = list(letterPile)
        position = list(map(int, position.split(" ")))
        position = [n - 1 for n in position]

        writer = ""
        for n in position:
            writer += letterPile[n]
        print(writer)

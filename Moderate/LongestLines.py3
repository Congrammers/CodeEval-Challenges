import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    amount = int(inFile.readline().rstrip())

    extracted = []
    for line in inFile:
        extracted.append(line.rstrip())

    extracted.sort(key=len, reverse=True)

    for index in range(amount):
        print(extracted[index])

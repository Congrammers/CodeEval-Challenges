import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        line = line.rstrip().split(',')
        countList = []

        start = 'X'
        end = 'Y'
        for seq in line:
            val = seq[seq.rfind(start) + 1: seq.find(end)]
            currCount = len(val)
            countList.append(currCount)

        print(min(countList))

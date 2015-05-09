import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        ori = line.rstrip()
        power = len(ori)
        digitList = map(int, ori)
        total = sum([n ** power for n in digitList])
        print(total == int(ori))

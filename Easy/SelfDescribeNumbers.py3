import sys

def isSelfDescribe(num):
    digitTable = [n for n in range(len(str(num)))]
    whole = list(map(int, list(str(num))))
    description = list(map(whole.count, digitTable))
    return int(whole == description)

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        print(isSelfDescribe(line.rstrip()))

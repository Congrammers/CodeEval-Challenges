import sys

def checkRotation(str1, str2):
    try:
        return (len(str1) == len(str2)) and ((str1 + str1).index(str2) != -1)
    except ValueError:
        return False

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        ori, rotated = line.rstrip().split(',')
        print(checkRotation(ori, rotated))

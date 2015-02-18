import sys
import math

def doubleSquare(num):
    result = []
    for y in range(int(math.sqrt(num))):
        x2 = num - y ** 2
        x = math.sqrt(x2)
        if y > x:
            break
        if x == int(x):
            result.append((int(x), y))

    return result

path = sys.argv[1]
with open(path, 'r') as inFile:
    skipTrash = inFile.readline()
    for line in inFile:
        line = line.rstrip()
        if line == "0":
            print(1)
        else:
            print(len(doubleSquare(float(line))))

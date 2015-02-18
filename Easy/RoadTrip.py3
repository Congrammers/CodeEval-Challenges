import sys
from collections import Counter

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        line = line.rstrip().split()
        line = [full.rstrip(';').split(',') for full in line]
        cityDistance = Counter({city: int(distnc) for city, distnc in line})

        currentPos = 0
        distanceDiff = []
        for city, distance in reversed(cityDistance.most_common()):
            distanceDiff.append(str(distance - currentPos))
            currentPos = distance
        print(",".join(distanceDiff))

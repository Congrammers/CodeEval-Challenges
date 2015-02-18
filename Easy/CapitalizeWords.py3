import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        line = list(line.rstrip().split(" "))
        print(" ".join(word[0].upper() + word[1:] for word in line))

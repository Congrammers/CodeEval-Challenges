import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        sentence, chosen = line.rstrip().split(',')
        chosenPos = len(sentence) - len(chosen)
        print(1 if sentence[chosenPos:] == chosen else 0)

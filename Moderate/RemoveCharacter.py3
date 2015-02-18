import re
import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        line = line.rstrip()
        sentence, target = line.split(', ')
        for c in target:
            sentence = sentence.replace(c, '')
        print(sentence)

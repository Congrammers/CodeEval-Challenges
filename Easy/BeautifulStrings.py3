import sys
from collections import Counter

def translateAndSum(sentence):
    caseIgnored = sentence.lower()
    letterList = list(map(chr, range(97, 123)))
    punctIgnored = list(''.join([c for c in caseIgnored if c in letterList]))

    countList = Counter()
    for letter in punctIgnored:
        countList[letter] += 1

    beautyness = 26
    total = 0
    for word, count in countList.most_common():
        total += (beautyness * count)
        beautyness -= 1
    return total

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        print(translateAndSum(line.rstrip()))

import sys

def checkLast(ref, word):
    for n in range(len(word)):
        now = n + 1
        if now not in ref:
            last = len(word)-1
            ref[now] = word[last]
            break

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        word, num = line.rstrip().split(';')
        word = word.split()
        num = list(map(int, num.split()))
        referential = dict(zip(num, word))

        checkLast(referential, word)

        result = []
        for n in range(len(referential)):
            now = n + 1
            result.append(referential[now])

        print(" ".join(result))

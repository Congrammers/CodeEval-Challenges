import sys

def reversedSentence(sentence):
    return " ".join(reversed(sentence))

firstArgs = sys.argv[1]
with open(firstArgs, 'r') as inFile:
    for line in inFile:
        wordList = line.rstrip().split(" ")
        print(reversedSentence(wordList))

import sys
from string import punctuation

punctMark = ['.', '!', '?']
def splitPunct(sentence):
    result = []
    senResult = ""
    for c in sentence:
        senResult += c
        if c in punctMark:
            result.append(senResult)
            senResult = ""
    return result


path = sys.argv[1]
with open(path, 'r') as inFile:
    slangCounter = 0
    slang = [", yeah!",
             ", this is crazy, I tell ya.",
             ", can U believe this?",
             ", eh?",
             ", aw yea.",
             ", yo.",
             "? No way!",
             ". Awesome!"]
    flipflop = True

    for line in inFile:
        line = splitPunct(line.rstrip())

        for sentence in line:
            if flipflop:
                flipflop = False
            else:
                oriPos = line.index(sentence)
                if sentence[-1] in punctuation:
                    sentence = sentence[:-1]

                altered = sentence + slang[slangCounter]
                slangCounter += 1
                if slangCounter == len(slang):
                    slangCounter = 0

                line[oriPos] = altered
                flipflop = True

        print("".join(line))

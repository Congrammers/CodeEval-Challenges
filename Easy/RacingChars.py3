import sys

def choose(line):
        if 'C' in line:
            return ('C', line.index('C'))
        elif '_' in line:
            return ('_', line.index('_'))
        else:
            raise(ValueError)


path = sys.argv[1]
with open(path, 'r') as inFile:

    carPos = None
    for line in inFile:
        line = line.rstrip()
        chosen, chosenPos = choose(line)
        if not carPos:
            result = line.replace(chosen, '|')
        elif chosenPos == carPos:
            result = line.replace(chosen, '|')
        elif chosenPos > carPos:
            result = line.replace(chosen, '\\')
        elif chosenPos < carPos:
            result = line.replace(chosen, '/')

        carPos = chosenPos
        print(result)

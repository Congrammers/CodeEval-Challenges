import sys

def multiOf(val, multi):
    return val % multi == 0

def ProcessBatch(fiDiv, buDiv, sampleSize):
    oriList = [i + 1 for i in range(sampleSize)]
    result = " ".join(['FB' if multiOf(n, fiDiv) and multiOf(n, buDiv) else
                       'F' if multiOf(n, fiDiv) else
                       'B' if multiOf(n, buDiv) else
                       str(n) for n in oriList])
    return result + '\n'

firstArgs = sys.argv[1]
with open(firstArgs, 'r') as inFile:
    for batch in inFile:
        X, Y, N = map(int, batch.rstrip().split(" "))
        print (ProcessBatch(X, Y, N))

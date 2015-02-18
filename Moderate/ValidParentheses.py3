import sys

def isWellFormed(val):
    prev = ""
    while (len(val) != len(prev)):
        prev = val
        val = val.replace("()", "")\
            .replace("[]", "")\
            .replace("{}", "")
    return (len(val) == 0)

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        print(isWellFormed(line.rstrip()))

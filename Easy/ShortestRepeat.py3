import sys
import re

def repetition(s):
    r = re.compile(r"(.+?)\1+")
    for match in r.finditer(s):
        yield (match.group(1), len(match.group(0))/len(match.group(1)))

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        line = line.rstrip()
        translated = list(repetition(line))
        result, trash = translated[0] if translated else (None, None)

        if not result:
            print(len(line))
        else:
            print(len(result))

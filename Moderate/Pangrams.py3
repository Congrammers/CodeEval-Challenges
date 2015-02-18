import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    letterSet = 'abcdefghijklmnopqrstuvwxyz'
    is_pangram = lambda s: not set(letterSet) - set(s)
    for line in inFile:
        line = line.rstrip().lower()
        if is_pangram(line):
            print("NULL")
        else:
            result = ""
            for char in letterSet:
                if char not in line:
                    result += char
            print(result)

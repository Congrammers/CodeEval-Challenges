import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        line = line.rstrip()

        flipflop = True
        result = ""
        for char in line:
            if char.isalpha():
                if flipflop:
                    result += char.upper()
                    flipflop = False
                else:
                    result += char.lower()
                    flipflop = True
            else:
                result += char

        print(result)

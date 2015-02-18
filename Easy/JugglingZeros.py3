import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        switcher = None
        line = line.rstrip().split()

        result = ""
        for val in line:
            if not switcher:
                switcher = val
            elif switcher == "0":
                result += val
                switcher = None
            elif switcher == "00":
                result += "".join(["1" for n in val])
                switcher = None
            else:
                raise(ValueError)
        print(int(result, 2))

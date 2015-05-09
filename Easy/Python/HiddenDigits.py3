import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        frm = 'abcdefghij'
        to = '0123456789'
        transTable = str.maketrans(frm, to)
        result = line.rstrip().translate(transTable)
        result = ''.join(w for w in result if w.isdigit())

        print(result if result else "NONE")

import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        line = list(line.rstrip())

        upper = 0
        lower = 0
        for letter in line:
            if letter.isupper():
                upper += 1
            if letter.islower():
                lower += 1

        upPerc = upper/len(line) * 100
        lowPerc = lower/len(line) * 100
        print("lowercase:", "{:.2f}".format(lowPerc),
              "uppercase:", "{:.2f}".format(upPerc))

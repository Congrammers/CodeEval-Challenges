import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        line = list(line.rstrip().split(','))
        word = [w for w in line if not w.isdigit()]
        number = [n for n in line if n.isdigit()]
        result = ','.join(word)
        result += '|' + ','.join(number) if word and number\
            else ','.join(number)
        print(result)

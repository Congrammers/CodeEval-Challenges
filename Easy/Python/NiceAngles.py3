import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        line = float(line.rstrip())
        degree = int(line)
        minute = int((line - degree) * 60)
        second = int((line - degree - minute / float(60)) * 3600)

        result = str(degree) + '.' + str(minute).zfill(2) + "'" +\
            str(second).zfill(2) + '"'
        print(result)

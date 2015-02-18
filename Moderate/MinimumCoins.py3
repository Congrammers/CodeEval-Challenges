import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    coin = [5, 3, 1]
    for line in inFile:
        n = int(line.rstrip())

        counter = 0
        for c in coin:
            while n != 0:
                if c > n:
                    break
                n -= c
                counter += 1
        print(counter)

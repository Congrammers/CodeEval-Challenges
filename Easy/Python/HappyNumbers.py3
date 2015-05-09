import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        n = int(line.rstrip())
        while (True):
            if (n == 1):
                print(1)
                break
            if (n == 4):
                print(0)
                break

            digitList = map(int, list(str(n)))
            n = sum([i ** 2 for i in digitList])

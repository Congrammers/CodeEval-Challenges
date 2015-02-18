import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        people, step = line.rstrip().split(',')
        people = [n for n in range(int(people))]
        step = int(step) - 1

        counter = 0
        result = []
        while len(people) != 0:
            counter += step
            while counter >= len(people):
                counter %= len(people)
            result.append(people.pop(counter))
        print(" ".join(list(map(str, result))))

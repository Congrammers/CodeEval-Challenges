import sys

def calculate(value, operation):
    if '+' in operation:
        first, trash = operation.split('+')
        first = value[:len(first)]
        second = value[len(first):]

        first = int(first)
        second = int(second)
        return first + second
    elif '-' in operation:
        first, trash = operation.split('-')
        first = value[:len(first)]
        second = value[len(first):]

        first = int(first)
        second = int(second)
        return first - second
    else:
        raise(ValueError)

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        value, operation = line.rstrip().split()
        print(calculate(value, operation))

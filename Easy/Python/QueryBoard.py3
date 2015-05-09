import sys

cols_count = 256
rows_count = 256
board = [[0 for j in range(cols_count)] for i in range(rows_count)]

def setRow(val, row, matrix):
    for j in range(cols_count):
        matrix[row][j] = val
def setCol(val, col, matrix):
    for i in range(rows_count):
        matrix[i][col] = val

def queryRow(row, matrix):
    total = 0
    for j in range(cols_count):
        total += matrix[row][j]
    return total
def queryCol(col, matrix):
    total = 0
    for i in range(rows_count):
        total += matrix[i][col]
    return total

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        lineList = list(line.rstrip().split(" "))
        operation = lineList.pop(0)
        lineList = list(map(int, lineList))

        if operation == "SetCol":
            pos, val = lineList
            setCol(val, pos, board)
        elif operation == "SetRow":
            pos, val = lineList
            setRow(val, pos, board)
        elif operation == "QueryCol":
            pos = lineList.pop()
            print(queryCol(pos, board))
        elif operation == "QueryRow":
            pos = lineList.pop()
            print(queryRow(pos, board))

#    for row in board:
#        print(row)

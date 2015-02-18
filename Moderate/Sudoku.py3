import sys
import math
import itertools

def sudoku_ok(line, size):
    return (len(line) == size and sum(line) == sum(set(line)))

def check_sudoku(grid, size):
    bad_rows = [row for row in grid if not sudoku_ok(row, size)]
    grid = list(zip(*grid))
    bad_cols = [col for col in grid if not sudoku_ok(col, size)]
    squares = []

    st = int(math.sqrt(float(size)))
    for i in range(0, size, st):
        for j in range(0, size, st):
            square = list(itertools.chain(row[j:j+st] for row in grid[i:i+st]))
            squares.append(square)
    bad_squares = [squa for squa in squares if not
                   sudoku_ok(list(itertools.chain.from_iterable(squa)), size)]
    return not (bad_rows or bad_cols or bad_squares)

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        N, listing = line.rstrip().split(';')
        N = int(N)
        listing = list(map(int, listing.split(',')))

        matrixed = [[listing[x+y*N] for x in range(N)]
                    for y in range(N)]
        print(check_sudoku(matrixed, N))

import sys

boardX = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
boardY = ['1', '2', '3', '4', '5', '6', '7', '8']
possibleMoves = [[-1, 2], [1, 2],
                 [2, 1], [2, -1],
                 [-1, -2], [1, -2],
                 [-2, 1], [-2, -1]]

def getPossibleMoves(X, Y):
    result = []
    for deltaX, deltaY in possibleMoves:
        try:
            resX = boardX[X - deltaX]
            resY = boardY[Y - deltaY]
            if Y-deltaY < 0 or X-deltaX < 0:
                raise IndexError
            result.append((resX + resY))
        except IndexError:
            pass

    return sorted(result)

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        x, y = list(line.rstrip())
        posX = boardX.index(x)
        posY = boardY.index(y)

        print(" ".join(getPossibleMoves(posX, posY)))

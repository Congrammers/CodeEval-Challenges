import sys
from collections import namedtuple

Point = namedtuple("Point", "x y")
Rectangle = namedtuple("Rectangle", "left top right bottom")

def outSideCheck(a, b):
    return b.right < a.left or a.right < b.left
def outBottomUpCheck(a, b):
    return a.top < b.bottom or a.bottom > b.top

def overlapRect(a, b):
    return not(outSideCheck(a, b) or outBottomUpCheck(a, b))

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        coord = list(map(int, line.rstrip().split(',')))

        upLeftA = Point(x=coord[0], y=coord[1])
        lowRightA = Point(x=coord[2], y=coord[3])
        rectA = Rectangle(left=upLeftA.x, top=upLeftA.y,
                          right=lowRightA.x, bottom=lowRightA.y)
        upLeftB = Point(x=coord[4], y=coord[5])
        lowRightB = Point(x=coord[6], y=coord[7])
        rectB = Rectangle(left=upLeftB.x, top=upLeftB.y,
                          right=lowRightB.x, bottom=lowRightB.y)

        print(overlapRect(rectA, rectB))

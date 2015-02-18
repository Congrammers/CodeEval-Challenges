import sys
import os

firstArgs = sys.argv[1]
with open(firstArgs, 'r') as path:
    print(os.path.getsize(firstArgs))

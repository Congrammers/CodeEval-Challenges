from urllib.parse import urlparse
from urllib.parse import unquote
import sys

def checkPort(f, s):
    if f.port:
        fVal = f.port
    else:
        fVal = 80
    if s.port:
        sVal = s.port
    else:
        sVal = 80
    return sVal == fVal
def checkPath(f, s):
    fVal = unquote(f.path)
    sVal = unquote(s.path)
    return fVal == sVal
def checkHost(f, s):
    return f.hostname == s.hostname

def checkURI(f, s):
    return checkPort(f, s) and checkPath(f, s) and checkHost(f, s)

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        first, second = map(str.lower, line.rstrip().split(';'))
        first = urlparse(first)
        second = urlparse(second)
        print(checkURI(first, second))
